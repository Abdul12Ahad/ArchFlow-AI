from fastapi import APIRouter
from pydantic import BaseModel

from backend.app.services.embedding_service import embedding_model
from backend.app.services.vector_db_service import collection
from backend.app.services.llm_service import generate_response

router = APIRouter()


class QueryRequest(BaseModel):
    query: str


# =========================================
# GENERATE DYNAMIC DIAGRAM
# =========================================

def generate_diagram(query: str, documents, dependency_graph):

    query = query.lower()

    edges = []

    # =====================================
    # AUTH / LOGIN FLOW
    # =====================================

    if (
        "auth" in query
        or "login" in query
        or "jwt" in query
        or "authentication" in query
    ):

        for edge in dependency_graph:

            source = edge["source"]
            target = edge["target"]

            if (
                "auth" in source.lower()
                or "auth" in target.lower()
                or "jwt" in target.lower()
                or "login" in target.lower()
            ):

                edges.append((source, target))

    # =====================================
    # API / ROUTE FLOW
    # =====================================

    elif (
        "api" in query
        or "route" in query
        or "backend" in query
    ):

        for edge in dependency_graph:

            source = edge["source"]
            target = edge["target"]

            if (
                "api" in source.lower()
                or "route" in source.lower()
                or "router" in source.lower()
                or "endpoint" in target.lower()
            ):

                edges.append((source, target))

    # =====================================
    # DATABASE FLOW
    # =====================================

    elif (
        "database" in query
        or "db" in query
        or "mongo" in query
        or "sql" in query
    ):

        for edge in dependency_graph:

            source = edge["source"]
            target = edge["target"]

            if (
                "db" in target.lower()
                or "database" in target.lower()
                or "mongo" in target.lower()
                or "sql" in target.lower()
            ):

                edges.append((source, target))

    # =====================================
    # EXECUTION FLOW
    # =====================================

    elif (
        "flow" in query
        or "execution" in query
        or "process" in query
    ):

        for edge in dependency_graph[:25]:

            edges.append((
                edge["source"],
                edge["target"]
            ))

    # =====================================
    # DEFAULT DEPENDENCY GRAPH
    # =====================================

    else:

        for edge in dependency_graph[:40]:

            edges.append((
                edge["source"],
                edge["target"]
            ))

    # =====================================
    # EMPTY SAFETY
    # =====================================

    if not edges:

        edges = [
            ("Frontend", "API"),
            ("API", "Services"),
            ("Services", "Database")
        ]

    # =====================================
    # BUILD MERMAID
    # =====================================

    mermaid = "graph TD\n"

    added = set()

    for start, end in edges:

        start = (
            start
            .replace("-", "_")
            .replace(".", "_")
            .replace("/", "_")
        )

        end = (
            end
            .replace("-", "_")
            .replace(".", "_")
            .replace("/", "_")
        )

        key = f"{start}->{end}"

        if key not in added:

            mermaid += f"{start} --> {end}\n"
            added.add(key)

    return mermaid


# =========================================
# ASK QUERY
# =========================================

@router.post("/ask")
def ask_query(request: QueryRequest):

    query_embedding = embedding_model.encode(
        request.query
    ).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=10
    )

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]

    dependency_graph = []

    # =====================================
    # EXTRACT RELATIONSHIPS
    # =====================================

    for doc in documents:

        lines = doc.splitlines()

        current_file = "Unknown"

        for line in lines:

            line = line.strip()

            # FILE
            if line.startswith("FILE:"):

                current_file = (
                    line.replace("FILE:", "")
                    .strip()
                )

            # IMPORTS
            if line.startswith("IMPORTS:"):

                imports = (
                    line.replace("IMPORTS:", "")
                    .strip()
                    .split(",")
                )

                for imp in imports:

                    imp = imp.strip()

                    if imp:

                        dependency_graph.append({
                            "source": current_file,
                            "target": imp
                        })

            # FUNCTION NAME
            if line.startswith("NAME:"):

                target = (
                    line.replace("NAME:", "")
                    .strip()
                )

                dependency_graph.append({
                    "source": current_file,
                    "target": target
                })

            # FUNCTION CALLS
            if line.startswith("CALLS:"):

                calls = (
                    line.replace("CALLS:", "")
                    .strip()
                    .split(",")
                )

                for call in calls:

                    call = call.strip()

                    if call:

                        dependency_graph.append({
                            "source": current_file,
                            "target": call
                        })

    # =====================================
    # BUILD CONTEXT
    # =====================================

    small_docs = []

    for doc in documents[:5]:

        small_docs.append(doc[:1500])

    context = "\n\n".join(small_docs)

    # =====================================
    # PROMPT
    # =====================================

    prompt = f"""
    You are an expert AI software architecture assistant.

    Your responsibilities:
    - Explain repository architecture
    - Explain execution flow
    - Explain API routes and backend flow
    - Explain dependencies and module relationships
    - Explain functions, classes, and services
    - Explain request lifecycle and control flow

    STRICT RULES:
    - ONLY use the provided repository context
    - DO NOT invent code or architecture
    - DO NOT hallucinate missing information
    - If context is insufficient, say:
    "Not enough repository context found."
    - Keep answers concise and repository-focused
    - Mention actual files/functions/classes if available
    - Distinguish between hooks, functions, classes, routes, and services correctly
    - Do not classify normal helper functions as React hooks
    - Explain repository-specific implementation details
    - Prefer concrete explanations over generic programming explanations
    - Explain flow step-by-step when relevant

    REPOSITORY CONTEXT:
    {context}

    USER QUESTION:
    {request.query}

    ANSWER:
    """

    ai_response = generate_response(prompt)

    diagram = generate_diagram(
        request.query,
        documents,
        dependency_graph
    )

    # =====================================
    # BUILD SOURCE SNIPPETS
    # =====================================

    sources = []
    seen = set()

    for index, doc in enumerate(documents[:5]):

        if doc in seen:
            continue

        seen.add(doc)
        metadata = {}

        if index < len(metadatas):
            metadata = metadatas[index]

        source = {
            "file": metadata.get(
                "file_path",
                "Unknown"
            ),
            "function": metadata.get(
                "name",
                "Unknown"
            ),
            "type": metadata.get(
                "type",
                "Unknown"
            ),
            "language": metadata.get(
                "language",
                "Unknown"
            ),
            "code": doc[:1200]
        }

        sources.append(source)

    return {
        "query": request.query,
        "answer": ai_response,
        "diagram": diagram,
        "sources": sources
    }
