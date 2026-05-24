from fastapi import APIRouter, HTTPException, BackgroundTasks
from pydantic import BaseModel

import uuid
import traceback
import os

from backend.app.services.github_service import clone_repository
from backend.app.services.parser_service import (
    scan_repository,
    extract_code_elements
)

from backend.app.services.chunking_service import create_chunks
from backend.app.services.embedding_service import generate_embedding
from backend.app.services.vector_db_service import store_chunk

router = APIRouter()

# =========================
# GLOBAL JOB STORAGE
# =========================

jobs = {}


class RepoRequest(BaseModel):
    repo_url: str


# =========================
# CREATE FOLDER TREE
# =========================

def build_file_tree(file_paths):

    tree = {}

    for path in file_paths:

        parts = path.replace("\\", "/").split("/")

        current = tree

        for part in parts:

            if part not in current:
                current[part] = {}

            current = current[part]

    return tree


# =========================
# BACKGROUND PROCESSOR
# =========================

def process_repository(job_id, repo_url):

    try:

        jobs[job_id]["status"] = "cloning"

        # Clone repository
        local_path = clone_repository(repo_url)

        jobs[job_id]["status"] = "scanning"

        # Scan files
        files = scan_repository(local_path)

        jobs[job_id]["total_files"] = len(files)

        total_chunks = 0
        processed_files = []
        file_data = {}
        dependency_graph = []


        # Process every file
        for index, file_path in enumerate(files):

            relative_path = (
                file_path
                .replace(local_path, "")
                .lstrip("/")
                .lstrip("\\")
            )

            relative_path = relative_path.replace("\\", "/")

            jobs[job_id]["current_file"] = relative_path
            jobs[job_id]["processed_count"] = index + 1

            print(f"[PROCESSING] {relative_path}")

            extracted_elements = extract_code_elements(file_path)

            # SAVE FILE FUNCTIONS / CLASSES
            file_data[relative_path] = extracted_elements

            # =====================================
            # BUILD DEPENDENCY GRAPH
            # =====================================

            for item in extracted_elements:

                if item["type"] == "imports":

                    imports = item["name"]

                    for imp in imports:

                        dependency_graph.append({
                            "source": relative_path,
                            "target": imp
                        })


            chunks = create_chunks(file_path, extracted_elements)

            for chunk in chunks:

                embedding_text = f"""
                Type: {chunk['type']}
                Name: {chunk['name']}
                File: {chunk['file_path']}
                Language: {chunk['language']}

                Code:
                {chunk['code']}
                """

                embedding = generate_embedding(embedding_text)

                metadata = {
                    "type": chunk["type"],
                    "name": chunk["name"],
                    "file_path": chunk["file_path"],
                    "language": chunk["language"]
                }

                chunk_id = str(uuid.uuid4())

                formatted_document = f"""
                FILE: {relative_path}

                TYPE: {chunk['type']}

                NAME: {chunk['name']}

                LANGUAGE: {chunk['language']}

                CODE:
                {chunk['code']}
                """

                store_chunk(
                chunk_id=chunk_id,
                embedding=embedding,
                metadata=metadata,
                document=formatted_document
                )


                total_chunks += 1

            processed_files.append(relative_path)

            jobs[job_id]["files"] = processed_files
            jobs[job_id]["chunks"] = total_chunks
            jobs[job_id]["file_data"] = file_data
            jobs[job_id]["tree"] = build_file_tree(processed_files)
            jobs[job_id]["dependency_graph"] = dependency_graph

        jobs[job_id]["status"] = "completed"

        print("[DONE] Repository Processing Completed")

    except Exception as e:

        print("[ERROR]", str(e))
        print(traceback.format_exc())

        jobs[job_id]["status"] = "failed"
        jobs[job_id]["error"] = str(e)


# =========================
# START INGESTION
# =========================

@router.post("/ingest")
def ingest_repo(
    data: RepoRequest,
    background_tasks: BackgroundTasks
):

    job_id = str(uuid.uuid4())

    jobs[job_id] = {
        "status": "starting",
        "files": [],
        "chunks": 0,
        "processed_count": 0,
        "total_files": 0,
        "current_file": "",
        "tree": {},
        "file_data": {}
    }

    background_tasks.add_task(
        process_repository,
        job_id,
        data.repo_url
    )

    return {
        "job_id": job_id
    }


# =========================
# CHECK STATUS
# =========================

@router.get("/status/{job_id}")
def get_status(job_id: str):

    if job_id not in jobs:

        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    return jobs[job_id]

