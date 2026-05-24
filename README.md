index.html:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>AI Codebase Explainer</title>

    <link rel="stylesheet" href="style.css" />

    <!-- Google Font -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>

    <!-- TOP NAVBAR -->
    <header class="top-navbar">
        <div class="logo-section">
            <div class="logo-circle"></div>
            <h1>AI Codebase Explainer</h1>
        </div>

        <div class="repo-input-section">
            <input
                type="text"
                id="repoUrl"
                placeholder="Enter GitHub Repository URL"
            />

            <button id="analyzeBtn">
                Analyze Repository
            </button>
        </div>
    </header>


    <!-- MAIN LAYOUT -->
    <main class="main-layout">

        <!-- LEFT PANEL -->
        <aside class="left-panel panel">
            <div class="panel-title">
                Repository Explorer
            </div>

            <div class="panel-content file-structure">

                <div class="folder">
                    📁 backend
                </div>

                <div class="nested">
                    📄 main.py
                    <br>
                    📄 query.py
                    <br>
                    📄 repo.py
                </div>

                <div class="folder">
                    📁 services
                </div>

                <div class="nested">
                    📄 parser_service.py
                    <br>
                    📄 embedding_service.py
                    <br>
                    📄 vector_db_service.py
                </div>

                <div class="folder">
                    📁 frontend
                </div>

                <div class="nested">
                    📄 index.html
                    <br>
                    📄 style.css
                    <br>
                    📄 script.js
                </div>

            </div>
        </aside>


        <!-- CENTER PANEL -->
        <section class="center-panel panel">

            <div class="panel-title">
                Repository Visualization
            </div>

            <div class="visualization-area">

                <div class="architecture-card">
                    <h2>Architecture Flow</h2>

                    <div class="flow-box">
                        Frontend
                    </div>

                    <div class="arrow">↓</div>

                    <div class="flow-box">
                        FastAPI Backend
                    </div>

                    <div class="arrow">↓</div>

                    <div class="flow-box">
                        RAG Retrieval System
                    </div>

                    <div class="arrow">↓</div>

                    <div class="flow-box">
                        Ollama + LLM
                    </div>

                    <div class="arrow">↓</div>

                    <div class="flow-box">
                        AI Repository Explanation
                    </div>
                </div>

            </div>

        </section>


        <!-- RIGHT PANEL -->
        <aside class="right-panel panel">

            <div class="panel-title">
                AI Context & Insights
            </div>

            <div class="context-card">
                <h3>Retrieved Function</h3>

                <p>
                    <span class="highlight">auth.py</span>
                    → generate_token()
                </p>
            </div>

            <div class="context-card">
                <h3>Related Explanation</h3>

                <p>
                    JWT token generation logic detected.
                    Authentication pipeline connected to login route.
                </p>
            </div>

            <div class="context-card">
                <h3>Semantic Match</h3>

                <p>
                    Query relevance score:
                    <span class="highlight">0.91</span>
                </p>
            </div>

        </aside>

    </main>


    <!-- BOTTOM CHAT PANEL -->
    <section class="chat-panel">

        <div class="chat-header">
            Ask Questions About Repository
        </div>

        <div class="chat-messages">

            <div class="message ai-message">
                AI: Repository visualization loaded successfully.
            </div>

            <div class="message user-message">
                User: Explain authentication flow.
            </div>

            <div class="message ai-message">
                AI: Authentication starts from login route,
                validates user credentials, generates JWT token,
                and returns authentication response.
            </div>

        </div>

        <div class="chat-input-area">
            <input
                type="text"
                placeholder="Ask repository-related questions..."
            />

            <button>
                Send
            </button>
        </div>

    </section>


    <script src="script.js"></script>

</body>
</html>

style.css:
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Poppins', sans-serif;
    background: #07111f;
    color: #ffffff;
    height: 100vh;
    overflow: hidden;
}

/* NAVBAR */

.top-navbar {
    height: 80px;
    width: 100%;
    padding: 0 30px;

    display: flex;
    align-items: center;
    justify-content: space-between;

    background: rgba(10, 18, 35, 0.95);
    border-bottom: 1px solid rgba(255,255,255,0.08);

    backdrop-filter: blur(10px);
}

.logo-section {
    display: flex;
    align-items: center;
    gap: 15px;
}

.logo-circle {
    width: 18px;
    height: 18px;
    border-radius: 50%;

    background: linear-gradient(135deg, #00d4ff, #7b61ff);

    box-shadow: 0 0 15px rgba(0,212,255,0.8);
}

.logo-section h1 {
    font-size: 24px;
    font-weight: 600;
}

.repo-input-section {
    display: flex;
    align-items: center;
    gap: 15px;
}

.repo-input-section input {
    width: 420px;
    padding: 14px 18px;

    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 12px;

    background: rgba(255,255,255,0.05);
    color: white;

    outline: none;

    font-size: 14px;
}

.repo-input-section input::placeholder {
    color: rgba(255,255,255,0.45);
}

.repo-input-section button {
    padding: 14px 22px;

    border: none;
    border-radius: 12px;

    background: linear-gradient(135deg, #00d4ff, #7b61ff);

    color: white;
    font-weight: 600;

    cursor: pointer;

    transition: 0.3s ease;
}

.repo-input-section button:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 20px rgba(0,212,255,0.25);
}

/* MAIN LAYOUT */

.main-layout {
    display: grid;
    grid-template-columns: 22% 1fr 24%;
    gap: 20px;

    height: calc(100vh - 240px);

    padding: 20px;
}

.panel {
    background: rgba(255,255,255,0.04);

    border: 1px solid rgba(255,255,255,0.06);

    border-radius: 20px;

    backdrop-filter: blur(10px);

    overflow: hidden;
}

.panel-title {
    padding: 18px 20px;

    font-size: 17px;
    font-weight: 600;

    border-bottom: 1px solid rgba(255,255,255,0.06);

    background: rgba(255,255,255,0.03);
}

/* LEFT PANEL */

.file-structure {
    padding: 20px;

    line-height: 2;

    color: rgba(255,255,255,0.88);
}

.folder {
    font-weight: 600;
    margin-top: 12px;
}

.nested {
    margin-left: 18px;
    color: rgba(255,255,255,0.7);
}

/* CENTER PANEL */

.visualization-area {
    height: 100%;

    display: flex;
    justify-content: center;
    align-items: center;

    padding: 30px;
}

.architecture-card {
    width: 100%;
    max-width: 500px;

    background: rgba(255,255,255,0.03);

    border-radius: 20px;

    padding: 35px;

    border: 1px solid rgba(255,255,255,0.06);

    text-align: center;
}

.architecture-card h2 {
    margin-bottom: 30px;

    color: #00d4ff;

    font-size: 26px;
}

.flow-box {
    padding: 16px;

    border-radius: 14px;

    background: linear-gradient(135deg, rgba(0,212,255,0.15), rgba(123,97,255,0.15));

    border: 1px solid rgba(255,255,255,0.08);

    font-weight: 500;

    margin: 10px 0;
}

.arrow {
    font-size: 28px;

    margin: 10px 0;

    color: #00d4ff;
}

/* RIGHT PANEL */

.right-panel {
    padding-bottom: 20px;
}

.context-card {
    margin: 20px;
    padding: 18px;

    border-radius: 16px;

    background: rgba(255,255,255,0.04);

    border: 1px solid rgba(255,255,255,0.05);
}

.context-card h3 {
    margin-bottom: 12px;

    color: #00d4ff;

    font-size: 16px;
}

.context-card p {
    line-height: 1.8;

    color: rgba(255,255,255,0.8);

    font-size: 14px;
}

.highlight {
    color: #7b61ff;
    font-weight: 600;
}

/* CHAT PANEL */

.chat-panel {
    height: 220px;

    margin: 0 20px 20px 20px;

    background: rgba(255,255,255,0.04);

    border-radius: 20px;

    border: 1px solid rgba(255,255,255,0.06);

    display: flex;
    flex-direction: column;

    overflow: hidden;
}

.chat-header {
    padding: 18px 22px;

    font-weight: 600;

    border-bottom: 1px solid rgba(255,255,255,0.06);
}

.chat-messages {
    flex: 1;

    padding: 18px;

    overflow-y: auto;
}

.message {
    margin-bottom: 14px;

    padding: 14px 18px;

    border-radius: 14px;

    max-width: 75%;

    line-height: 1.7;

    font-size: 14px;
}

.ai-message {
    background: rgba(0,212,255,0.1);

    border: 1px solid rgba(0,212,255,0.18);
}

.user-message {
    margin-left: auto;

    background: rgba(123,97,255,0.14);

    border: 1px solid rgba(123,97,255,0.18);
}

.chat-input-area {
    padding: 16px;

    display: flex;
    gap: 12px;

    border-top: 1px solid rgba(255,255,255,0.06);
}

.chat-input-area input {
    flex: 1;

    padding: 14px 16px;

    border-radius: 12px;

    border: 1px solid rgba(255,255,255,0.08);

    background: rgba(255,255,255,0.04);

    color: white;

    outline: none;
}

.chat-input-area button {
    padding: 14px 20px;

    border: none;
    border-radius: 12px;

    background: linear-gradient(135deg, #00d4ff, #7b61ff);

    color: white;

    font-weight: 600;

    cursor: pointer;

    transition: 0.3s ease;
}

.chat-input-area button:hover {
    transform: translateY(-2px);
}

/* RESPONSIVE */

@media (max-width: 1200px) {

    .main-layout {
        grid-template-columns: 1fr;
        height: auto;
    }

    body {
        overflow-y: auto;
    }

    .chat-panel {
        height: auto;
        min-height: 280px;
    }

    .repo-input-section {
        flex-direction: column;
        width: 100%;
    }

    .repo-input-section input {
        width: 100%;
    }

    .top-navbar {
        flex-direction: column;
        height: auto;
        gap: 20px;
        padding: 20px;
    }
}

script.js:
window.addEventListener("DOMContentLoaded", () => {

    console.log("AI Codebase Explainer Frontend Loaded");

    const analyzeBtn = document.getElementById("analyzeBtn");

    const chatMessages = document.querySelector(".chat-messages");

    console.log("Analyze Button:", analyzeBtn);

    analyzeBtn.addEventListener("click", async () => {

        console.log("BUTTON CLICKED");

        const repoUrl = document.getElementById("repoUrl").value;

        if (!repoUrl) {
            alert("Please enter a GitHub repository URL");
            return;
        }

        try {

            analyzeBtn.innerText = "Processing...";

            addAIMessage("Cloning repository...");
            addAIMessage("Scanning repository files...");
            addAIMessage("Generating semantic embeddings...");

            console.log("Sending request...");

            const response = await fetch(
                "http://192.168.56.1:8000/repo/ingest",
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        repo_url: repoUrl
                    })
                }
            );

            console.log("Response:", response);

            const data = await response.json();

            console.log("DATA:", data);

            addAIMessage(
                `Repository processed successfully.`
            );

            addAIMessage(
                `Indexed ${data.total_files} files and stored ${data.total_chunks_stored} semantic chunks into ChromaDB.`
            );

            updateRepositoryExplorer(data.files);

            updateInsights(data);

            updateVisualization();

        } catch (error) {

            console.error("ERROR:", error);

            addAIMessage("Error processing repository.");

        } finally {

            analyzeBtn.innerText = "Analyze Repository";
        }

    });

    function updateRepositoryExplorer(files) {

        const explorer = document.querySelector(".file-structure");

        explorer.innerHTML = "";

        files.forEach(file => {

            const fileDiv = document.createElement("div");

            fileDiv.classList.add("nested");

            fileDiv.innerHTML = `📄 ${file}`;

            explorer.appendChild(fileDiv);

        });
    }

    function addAIMessage(message) {

        const messageDiv = document.createElement("div");

        messageDiv.classList.add("message");
        messageDiv.classList.add("ai-message");

        messageDiv.innerText = `AI: ${message}`;

        chatMessages.appendChild(messageDiv);

        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    function updateInsights(data) {

        const rightPanel = document.querySelector(".right-panel");

        rightPanel.innerHTML = `

            <div class="panel-title">
                AI Context & Insights
            </div>

            <div class="context-card">
                <h3>Total Files</h3>

                <p>
                    <span class="highlight">
                        ${data.total_files}
                    </span>
                </p>
            </div>

            <div class="context-card">
                <h3>Total Chunks</h3>

                <p>
                    <span class="highlight">
                        ${data.total_chunks_stored}
                    </span>
                </p>
            </div>

        `;
    }

    function updateVisualization() {

        const visualizationArea = document.querySelector(".visualization-area");

        visualizationArea.innerHTML = `

            <div class="architecture-card">

                <h2>Repository Processed Successfully</h2>

                <div class="flow-box">GitHub Repository</div>

                <div class="arrow">↓</div>

                <div class="flow-box">Repository Cloned</div>

                <div class="arrow">↓</div>

                <div class="flow-box">Code Parsed</div>

                <div class="arrow">↓</div>

                <div class="flow-box">Embeddings Generated</div>

                <div class="arrow">↓</div>

                <div class="flow-box">Stored in ChromaDB</div>

            </div>

        `;
    }

});

repo.py:
from fastapi import APIRouter
from pydantic import BaseModel
import uuid

from backend.app.services.github_service import clone_repository
from backend.app.services.parser_service import (
    scan_repository,
    extract_code_elements
)

from backend.app.services.chunking_service import create_chunks
from backend.app.services.embedding_service import generate_embedding
from backend.app.services.vector_db_service import store_chunk

router = APIRouter()


class RepoRequest(BaseModel):
    repo_url: str


@router.post("/ingest")
def ingest_repo(data: RepoRequest):

    # Clone Repository
    local_path = clone_repository(data.repo_url)

    # Scan Repository
    files = scan_repository(local_path)

    total_chunks = 0

    # Store relative file paths for frontend
    relative_files = []

    # Process Files
    for file_path in files:

        # Add relative path
        relative_path = file_path.replace(local_path, "")
        relative_files.append(relative_path)

        # Extract functions/classes/methods
        extracted_elements = extract_code_elements(file_path)

        if not extracted_elements:
            continue

        # Create semantic chunks
        chunks = create_chunks(file_path, extracted_elements)

        # Process each chunk
        for chunk in chunks:

            # Better embedding context
            embedding_text = f"""
            Type: {chunk['type']}
            Name: {chunk['name']}
            File: {chunk['file_path']}
            Language: {chunk['language']}

            Code:
            {chunk['code']}
            """

            # Generate embedding
            embedding = generate_embedding(embedding_text)

            # Metadata
            metadata = {
                "type": chunk["type"],
                "name": chunk["name"],
                "file_path": chunk["file_path"],
                "language": chunk["language"]
            }

            # Store in ChromaDB
            store_chunk(
                chunk_id=str(uuid.uuid4()),
                embedding=embedding,
                metadata=metadata,
                document=chunk["code"]
            )

            total_chunks += 1

    return {
    "message": "Repository processed successfully",
    "total_files": len(files),
    "total_chunks_stored": total_chunks,

    "files": [
        file.replace(local_path, "")
        for file in files
    ]
    }

github_service.py:
import os
from git import Repo

REPO_BASE_PATH = "repositories"

def clone_repository(repo_url: str):

    repo_name = repo_url.split("/")[-1].replace(".git","")

    local_path = os.path.join(REPO_BASE_PATH, repo_name)

    if os.path.exists(local_path):
        return local_path
    
    Repo.clone_from(repo_url, local_path)

    return local_path

main.py:
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.api.routes.repo import router as repo_router
from backend.app.api.routes.query import router as query_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(repo_router, prefix="/repo")
app.include_router(query_router, prefix="/query")


@app.get("/")
def home():
    return {"message": "AI Codebase Explainer Backend Running"}


vs code output:
Stored chunk: 1c2a6e5d-0c01-4ec0-99eb-5e298f28a26f
Stored chunk: 08f30438-8321-4aa4-a4dd-36a5e311d3b7
Stored chunk: acb7f7e6-46db-478e-8433-a3f64802d507
Stored chunk: 72d02e7a-957a-46ca-a25a-aa0bd665924b
Stored chunk: 2a9831d4-29a6-4cdf-8546-4084ebf890ef
Stored chunk: d16da677-40d3-4b81-a1d5-f27dedb43e4b
Stored chunk: a580baa0-e77d-440e-9492-eaeea4457400
Stored chunk: 18e35938-fa9e-4ddd-8689-6f503bef5fe9
Stored chunk: 9d725221-a94b-43b8-8a0f-1f566144833e
Stored chunk: 4e0ce6e5-07c9-4197-9811-7381b20cf216
Stored chunk: 7ffa8a50-057a-4d8c-a7d1-41a3819cab38
Stored chunk: 04e7e33f-8c8c-43ad-8d82-cfa9604a06c9
Stored chunk: 5cc1b8a7-a670-4768-bc17-70da51b51952
Stored chunk: cd6c007d-8775-4945-849c-613f188edc8a
Stored chunk: 23a9e2a2-5bf3-43f5-a8a7-b77b311d5045
Stored chunk: bf13c144-1fac-4ff1-b158-cc6b5333533c
Stored chunk: 496778e0-8a76-4ac1-89b7-0fbf8f2a773b
Stored chunk: 36af68be-f527-441a-a7d8-e0703fea1392
Stored chunk: 7b7ce735-8184-4943-87d5-7bfdbe57d3f3
Stored chunk: eb366e7b-5840-462c-853a-3794b80f10d8
Stored chunk: 6a0fffd3-a239-452d-90d7-db369a5c6bb5
Stored chunk: 128c14e4-1313-40a9-b573-98deb1305051
Stored chunk: ae220103-90ae-4ebf-ac65-e1694ba7db3e
Stored chunk: 7b0e96c2-3b7b-4527-a296-15abb89b0dbc
Stored chunk: 2d3c40c6-f88d-4e22-b4e7-8436c56f2515
Stored chunk: 5621c7b4-c8bd-46ed-a6b2-dba7366fc6c2
Stored chunk: 8447a706-684e-446e-a0f5-09615b84602b
Stored chunk: b9640946-ae2c-475b-a48a-c6da425e654a
Stored chunk: 22718a98-d6aa-408f-9440-549c9b5b7d1a
Stored chunk: 50377281-d37b-46b2-b3a2-24c8ec52ace4
Stored chunk: 9d33241f-931c-4b95-b126-0ed18afb046e
Stored chunk: 12ce6658-9e5c-4cf1-afde-5a7dc523eb55
Stored chunk: f6fd8571-5f90-4ff5-b72f-cae6b27e2732
Stored chunk: c15581a2-1722-46fd-9745-e0e7d489cf28
Stored chunk: 8114d25c-e81f-4703-b9cf-347d1a31437b
Stored chunk: c42ec863-b656-4822-a31b-837eb32c88cb
Stored chunk: 8c8fe597-818e-4a8b-930d-7d4a169dfc66
Stored chunk: 2187c6f2-387c-40c6-92bd-84b693ccb050
Stored chunk: 49592425-45a3-4fa1-836b-4dde8a2f4936
Stored chunk: abef4340-a9eb-4f7e-8633-e13c836b586d
Stored chunk: 3da5c7b3-9849-400a-92d1-47a14cd9c4b1
Stored chunk: 988d4055-6d48-4858-8084-aab147918e24
Stored chunk: 000fcb8e-9151-4b59-8ab3-cd57a21bc094
Stored chunk: 39a7c099-bb83-4e92-a45a-04d7cf298958
Stored chunk: e206ddee-97d2-44d9-957f-03c9a35e466d
Stored chunk: 5d20ae60-e1b9-450b-a01e-5eb1c0c20b1a
Stored chunk: aa2e6bc8-49a8-4718-841f-5ccade85d15d
Stored chunk: 82168a0b-5637-492a-aecf-4f93952e21f2
Stored chunk: 1c482fc8-35ea-4b16-94f9-3e31599af952
Stored chunk: ee707578-22f8-4d51-b503-e3f602d74d86
Stored chunk: 3f4e3ff0-6e12-4ce4-b5f7-94ef77a31981
Stored chunk: 681e0ac8-7b81-421b-a599-c40795c44cd8
Stored chunk: 8e0522dc-bb60-4d1c-ac9f-7d7f291e15d8
Stored chunk: 5bf17b9a-35e1-4288-9a7d-4d9c8787f3a2
Stored chunk: 3b86c7de-e8d3-4ced-a89e-5be359b5a9a6
Stored chunk: c1d3fe6d-90e7-4d6b-8ee3-effd7c0ed782
Stored chunk: e6990a5e-c9fd-4a3b-adef-192612b09c21
Stored chunk: 322e79a7-9358-4d8b-8669-76867172ddcc
Stored chunk: 73137aca-ed80-434b-abae-bfb26a771909
Stored chunk: 2e6d8d32-7dc6-4874-99c9-1189e6396a7f
Stored chunk: bf630a2e-78cf-4e55-a476-9791c3442936
Stored chunk: e586da55-23f9-45fe-a736-c7a8f47d99a3
Stored chunk: a81bec19-72ed-436c-84d4-efa56d48b782
Stored chunk: 7f384a7f-8258-43a8-a2d8-6558c832d098
Stored chunk: 56be4478-b71c-4df5-a788-4f55fa031af7
Stored chunk: bd663c94-f803-4027-9b21-aca05b397e11
Stored chunk: 6546b07d-fd9b-4d5c-9eb3-c868f357a649
Stored chunk: a1f4daf0-f798-4078-a339-e2c36059ecb3
Stored chunk: 5e2a838f-f5f8-4dcf-be9f-6fd1f9544188
Stored chunk: e7dc3c65-2e7a-4db5-93af-12472350267b
Stored chunk: 0c9f6870-f2ab-450a-ad3b-6892625ba32f
Stored chunk: 090c1f01-70f9-486e-aec7-a6d5727e9005
Stored chunk: e838649c-c6d3-450f-b86b-5bba14775d24
Stored chunk: 1f8c6642-9f20-41b9-8fba-fea90a7bd2ca
Stored chunk: b04fcdf2-37d0-4c69-9d71-0c39cb06bf92
Stored chunk: 0cbe9695-c72c-4040-a19c-5eb591ba27e7
Stored chunk: 188c0e16-1fef-41aa-a454-ae1c8051b042
Stored chunk: 95c7f058-6533-40b2-bf8c-8d828231925c
Stored chunk: 7f718148-d52c-4a66-9a2a-cfa943d67e2f
Stored chunk: e9ee2545-424f-4f5f-a438-98657fc83735
Stored chunk: 07bc1156-87bc-4db9-b2a6-cf605e67b344
Stored chunk: 14b2358a-05f3-4897-a7f5-644c87fab07f
Stored chunk: a3042350-654b-4da9-8b87-88851f6cae68
Stored chunk: 9cae36d1-9bac-4636-9a8e-b4013cc475fa
Stored chunk: bd91f4da-9273-4150-9733-ffd8e59b5fbc
Stored chunk: 9c8615a2-81a3-4aab-ad2e-569774faadab
Stored chunk: 680374ce-d8ff-4b3b-bf57-ee03a698d37b
Stored chunk: f32f3d36-d09c-4b0e-8a61-b0fac2345809
Stored chunk: e9ddd072-842b-43fb-8935-7657ddb1fa23
Stored chunk: 5c0c0fbb-a01e-48e0-8b9f-18a2dfbee75c
Stored chunk: b7a8493b-cf61-46d3-abbf-1480cf02ed6c
Stored chunk: 9f1b5ce1-2581-4214-bd4e-c26cce0c4211
Stored chunk: 32053bb1-d0f4-4b63-a2b5-709e0786e1e1
Stored chunk: a6374922-cc05-4ad8-8bb9-6a700086bdf3
Stored chunk: 841bb7f5-fe46-422e-b925-c680331c5a3c
Stored chunk: 6091a4f2-86e6-4ef8-bc94-637c7efecfda
Stored chunk: 980ab292-daee-4a3e-a1c3-379e82cb6754
Stored chunk: 3d2c292a-3254-473c-a314-1aa1fa892e95
Stored chunk: c2eea7c3-0c1b-443f-a70d-ce555fef394b
Stored chunk: e4819b54-eecd-4430-842e-4d0c96a68bcb
Stored chunk: dccd8ff5-73ee-4279-b8f5-d408f6f22b82
Stored chunk: bd41e619-7ddb-499d-aef7-3c42263e1fb7
Stored chunk: b6296eb8-7459-46f9-8559-1f5974718f2d
Stored chunk: fd2bd39f-3334-4ce4-93f6-e5e44372773a
Stored chunk: 1543511c-f0d2-4071-86a9-e64c2ebdcae3
Stored chunk: f51e8c8d-67fa-4422-b84a-e9f06b612cb2
Stored chunk: 5e145cae-ccf4-4f51-96c7-3caadd359b63
Stored chunk: 4922b1c5-9689-4000-98f4-7366f37ec5a3
Stored chunk: 6875b236-c1de-41a8-934c-38c50b9a065e
Stored chunk: 84b76e49-6733-4cc7-9cea-9394d127a32c
Stored chunk: d167b41d-1698-411f-a0ea-3bfcc3698c4c
Stored chunk: 8b6bd3e2-1dbb-4c86-89da-ecc4c27e5650
Stored chunk: c20f7e49-407e-481e-ace3-755adbc5dd17
Stored chunk: 604bee00-9af9-42b7-92b9-9165963c0de5
Stored chunk: cf670ed2-ecb8-4ff7-a652-8b077b11efa4
Stored chunk: 8fe13eb4-ccb7-4181-9bad-57ddf792e96a
Stored chunk: be647f0b-934c-42ff-81ae-57711a842855
Stored chunk: 7ad9bcc5-afd6-43db-8cdb-65760b376bbd
Stored chunk: 4c663ac3-2ee8-4c9a-99f0-7cadcfff65d7
Stored chunk: 5c1fc087-d95a-44b4-b230-e88719e6ab56
Stored chunk: 676524f7-af2c-4042-89f4-8451e83a7f8c
Stored chunk: 3655be75-2609-44cb-9b20-3d216c7ca927
Stored chunk: 5acb5d8e-2633-4ecf-a998-e14b142b7c6f
Stored chunk: 808e9344-c95b-4eb6-b207-ad12fd1ebe9e
Stored chunk: 2d51bdcf-fab1-40c1-b3f1-d94028c68414
Stored chunk: 14811e26-3edd-45b5-b2b4-347f726e3b6b
Stored chunk: 043ce896-aae7-4705-8c73-96bf27c5bee4
Stored chunk: 19969146-cd22-410d-8e9e-385ec823b2e5
Stored chunk: e7a794ef-8749-457d-b401-b0193081a687
Stored chunk: d3b6111c-0a62-46ae-8a36-4a0128021631
Stored chunk: 0d9d9ac9-34cd-43a4-b20b-b8bc5b505849
Stored chunk: cacc6653-6b09-4cef-ab13-f6a58d7a8910
Stored chunk: ed5fd725-ba6b-4df5-87c4-afe56903cad6
Stored chunk: a2ffb77a-eaec-40f8-8e96-d9c6a9a20abb
Stored chunk: 3bbd5fb0-f352-485e-b9de-7a06b0fe97d5
Stored chunk: 0c6ffd77-e090-4c6d-970e-b6435e1e5c48
Stored chunk: 22dacb70-5f88-4a50-8a04-8b80c55ddba4
Stored chunk: f478d7bc-84c7-4638-b9a8-d99c33a174a0
Stored chunk: 577323a1-cbc3-4f15-bbcc-cca925bce54d
Stored chunk: 980592b9-22d3-4614-a2e3-c1da5db3ce6c
Stored chunk: 79386ee0-5548-4a81-9d4e-0267e4f15c90
Stored chunk: ca5c6d33-cb83-4dfc-a56d-4b0e9c5a03f8
Stored chunk: 9a87c5c6-1250-4998-baea-847b96aae5cc
Stored chunk: 60670211-2bd3-417f-8ee6-8fd439111f31
Stored chunk: cc1bf3d4-2148-4bdc-b208-6d4daeb5fc71
Stored chunk: a5619c05-fbf0-40c8-9efc-94946d320bf6
Stored chunk: 4e4b69c2-36e1-406f-8602-3bcca5a3a541
Stored chunk: fbb4997d-06e1-4807-9e0f-c7ae406d6fe8
Stored chunk: d21b9186-2645-4ce2-9a80-28234563b8d0
Stored chunk: da83e81c-a645-430c-ac01-a58067c1efff
Stored chunk: 91e3eb61-2ea9-4158-a02f-33c734d408ef
Stored chunk: 8f49552e-bcba-404b-bd15-ed3585c7bd5f
Stored chunk: d14f85f0-5403-4bfb-b58f-b425b36d27b0
Stored chunk: aef93cf4-133f-43f5-849f-9615fe9fce83
Stored chunk: abb7db68-0129-462d-821b-59c1522c2874
Stored chunk: 5fa6b53f-ee89-4641-9bcb-2dc0e3ac8b22
Stored chunk: 3e78e20a-bf6e-4a45-b672-ad2c32502475
Stored chunk: 21c33a83-4045-4d7d-84af-7a4c573da8ce
Stored chunk: 648dc86b-9579-4016-aa19-886824e1408c
Stored chunk: 7fadc95e-908c-435c-ab9a-eea9434dc901
Stored chunk: 609ba78e-9405-4a21-b0de-9c1e49fca034
Stored chunk: dfd1b778-befc-4afe-9abc-32d70ba0f5c6
Stored chunk: 4056f9cb-28cd-475c-84f2-045d6a0eb2ad
Stored chunk: ff382ed9-3af8-4031-ab79-3854908cbbda
Stored chunk: d8d6d554-34f6-4b75-a76e-497b24ae0c9e
Stored chunk: e87949e6-113a-43d6-8617-652f3e2bdde0
Stored chunk: 0f04795d-8d1c-4e4c-b603-867fcd002ce7
Stored chunk: dd30d511-cfeb-4596-8245-3fc9d78ceeb7
Stored chunk: 78cd5ab9-cd86-4e20-b35f-a84d319feaf6
Stored chunk: aa17fd6f-871e-42ed-8c2e-9b51db02e328
Stored chunk: 6d93f70b-6da8-488b-a6c0-580b1b96fa8e
Stored chunk: 0fb725a3-7290-4382-8c7e-8f2f8fd11b61
Stored chunk: ff9a038c-bc41-4720-83c8-f5bb5e8a8052
Stored chunk: a9d98be5-acf9-494e-9593-6bfd5afe416c
Stored chunk: 494492af-28d5-48ac-926e-50ea175a4ed9
Stored chunk: 47a78c5d-ee68-44e6-9a01-d487b7c395f1
Stored chunk: 6c62b406-870b-487f-9601-9ba024db8f43
Stored chunk: c79d226a-43d0-4e23-957b-f42fa9fa5f7b
Stored chunk: e9468935-2b22-447b-a4ff-9f763d9fcacb
Stored chunk: 49d4b5a9-d5ab-4d66-8c43-610dc1757a59
Stored chunk: dc46dc41-739f-4041-bc5b-3f8c7b443705
Stored chunk: e5d59324-a3a8-4ecc-8fde-d7ab66ecda04
Stored chunk: 0e47f2c9-fde5-4a03-991d-8ca4dd35f6a0
Stored chunk: 8f3c70c3-9136-4b6e-b1f4-d0e4768e52b8
Stored chunk: de8ccd59-f47b-4ff8-ad82-936de579381d
Stored chunk: 2715c5c2-4e39-4467-a753-4739061eb1ae
Stored chunk: 60c7e496-0e41-48ee-aac1-38e2cd6c60f7
Stored chunk: d19726c8-b86a-4e56-b643-eb9ffdafa47e
Stored chunk: cd4c1501-8fce-4d66-8f17-90ea5ff983a5
Stored chunk: 22696399-fbf0-4924-8e9b-243828dcfcec
Stored chunk: a4bbdbdc-c617-4a9a-a11c-3f22c5066219
Stored chunk: 6cfdb000-29a6-442d-9204-f8b3bed7e126
Stored chunk: 954805d8-b0df-453a-8a5a-0f82a78af682
Stored chunk: 7965a24c-9fd2-4dea-985a-772d9c6b85d3
Stored chunk: ed15f6c9-843d-4a4b-b5ce-c637e2f09482
Stored chunk: 5be8962a-6683-4f05-80ee-5a7f3fd70453
Stored chunk: 628843b3-a22c-4dc7-97bd-b71fbca1d176
Stored chunk: f2af799d-c600-453a-b5c6-7a4dce2e6274
Stored chunk: 02481c3d-fefd-47a1-b699-bda2f9dfc0a0
Stored chunk: 25b7815a-12d2-4cf1-9f63-29e3624e233e
Stored chunk: 9c7e4151-4bb0-4b3d-b87f-3f1b522d99b3
Stored chunk: fd8649ed-1bbd-456c-842e-56e2e748c443
Stored chunk: 883ee5ae-7915-4d73-a9ba-52ac35851c42
Stored chunk: 045c0cdb-0f91-474d-8d5d-354bd66c473d
Stored chunk: 753ccad4-ac87-45a6-957d-3275786b7722
Stored chunk: 8fe74f33-cf32-497a-8acb-29c4eb99ff82
Stored chunk: b39bedde-1adf-4802-8bb9-0b81061923e9
Stored chunk: 18c0a8e5-6040-41d9-a9ba-8368983bff36
Stored chunk: 717f0b43-7f3e-423a-b802-aa49fda0be98
Stored chunk: 4a59591e-59a5-4fdd-a33d-021c98ecd80a
Stored chunk: c7babfba-75a5-455f-a7a3-35a068703dee
Stored chunk: 530d62f7-0809-43ac-aebb-07d20bb61862
Stored chunk: e4a8cdc0-c279-47ed-9c1c-7d5e1b163b7d
Stored chunk: e5fc013a-2dec-49f5-9d89-8374607369a1
Stored chunk: dde9212d-a56f-4947-99c8-ac5844bd11da
Stored chunk: ab7056dc-288c-4a62-bc63-b97807dc007d
Stored chunk: 6c5b621a-711d-4d18-a758-372c97eaf27b
Stored chunk: 55ca5aea-76b3-4162-8ded-99f4d71c7956
Stored chunk: 7c7517d5-3425-4e64-8ce1-f8c9fe4b5494
Stored chunk: 4864bb4c-dcbb-4dd6-ab51-b546d928367a
Stored chunk: ea3a9df9-ff6b-4b43-8fd0-8fb9c5dd8360
Stored chunk: c8e84c89-aad0-4c53-ab72-77fa494c067b
Stored chunk: 6da10f64-a010-47ec-a2b7-0a5171a34e63
Stored chunk: 075b3c74-0e70-44ae-9bdc-fd4a648d2848
Stored chunk: ed29763e-e973-43d2-9a9f-5fbdb5bab2b1
Stored chunk: 33b9364b-4b4d-45e1-9bfd-3ef29f4b4e25
Stored chunk: cac24ae1-1599-4d10-8949-5bfad3397a57
Stored chunk: 89621b81-17f0-40c0-8df5-b160da2e4f58
Stored chunk: 5d57958b-1d4d-4f7c-bde0-7a94769f7677
Stored chunk: fc36623c-5541-4d32-aefe-490a0e681e2f

browser console output:
AI Codebase Explainer Frontend Loaded
script.js:9 Analyze Button: <button id=​"analyzeBtn">​ Analyze Repository ​</button>​





index.html:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>AI Codebase Explainer</title>

    <link rel="stylesheet" href="style.css" />

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>

<body>

    <!-- TOP NAVBAR -->
    <header class="top-navbar">

        <div class="logo-section">
            <div class="logo-circle"></div>
            <h1>AI Codebase Explainer</h1>
        </div>

    </header>


    <!-- MAIN LAYOUT -->
    <main class="main-layout">

        <!-- LEFT PANEL -->
        <aside class="left-panel panel">

            <div class="panel-title">
                Repository Explorer
            </div>

            <div class="panel-content file-structure">

                <div class="empty-state">
                    Repository files will appear here
                </div>

            </div>

        </aside>


        <!-- CENTER PANEL -->
        <section class="center-panel panel">

            <div class="workspace-header">
                AI Workspace
            </div>

            <!-- HERO SECTION -->
<!-- TOP ACTION BAR -->
<div class="hero-section">

    <div class="hero-input">

        <input
            type="text"
            id="repoUrl"
            placeholder="Paste GitHub Repository URL"
            autocomplete="off"
        >

        <button
            id="analyzeBtn"
            type="button"
        >
            Analyze Repository
        </button>

    </div>

</div>

            <!-- MAIN OUTPUT AREA -->
            <div class="visualization-area">

                <div class="welcome-card">

                    <h2>Repository Visualization Workspace</h2>

                    <p>
                        Repository architecture, AI explanations,
                        semantic search results, dependency graphs,
                        and intelligent insights will appear here.
                    </p>

                </div>

            </div>

        </section>


        <!-- RIGHT PANEL -->
        <aside class="right-panel panel">

            <div class="panel-title">
                AI Context & Insights
            </div>

            <div class="insights-container">

                <div class="context-card">

                    <h3>Status</h3>

                    <p>
                        Waiting for repository analysis...
                    </p>

                </div>

            </div>

        </aside>

    </main>


    <!-- BOTTOM QUERY PANEL -->
    <section class="query-panel">

        <input
            type="text"
            id="queryInput"
            placeholder="Ask questions about repository..."
        >

        <button id="askBtn">
            Ask AI
        </button>

    </section>

    <script src="./script.js?v=999"></script>

</body>
</html>

style.css:
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Poppins', sans-serif;
    background: #07111f;
    color: white;

    height: 100vh;

    display: flex;
    flex-direction: column;

    overflow: hidden;
}

/* NAVBAR */

.top-navbar {
    height: 75px;

    display: flex;
    align-items: center;

    padding: 0 30px;

    border-bottom: 1px solid rgba(255,255,255,0.06);

    background: rgba(10, 18, 35, 0.95);

    backdrop-filter: blur(10px);
}

.logo-section {
    display: flex;
    align-items: center;
    gap: 15px;
}

.logo-circle {
    width: 18px;
    height: 18px;

    border-radius: 50%;

    background: linear-gradient(135deg, #00d4ff, #7b61ff);

    box-shadow: 0 0 20px rgba(0,212,255,0.7);
}

.logo-section h1 {
    font-size: 24px;
    font-weight: 600;
}

/* MAIN LAYOUT */

.main-layout {
    flex: 1;

    display: grid;
    grid-template-columns: 280px 1fr 300px;

    gap: 18px;

    padding: 18px;

    overflow: hidden;

    min-height: 0;
}

/* PANELS */

.panel {
    background: rgba(255,255,255,0.04);

    border: 1px solid rgba(255,255,255,0.06);

    border-radius: 20px;

    backdrop-filter: blur(12px);

    overflow: hidden;

    min-height: 0;
}

.panel-title,
.workspace-header {
    padding: 18px 22px;

    border-bottom: 1px solid rgba(255,255,255,0.06);

    font-size: 17px;
    font-weight: 600;

    background: rgba(255,255,255,0.03);
}

/* LEFT PANEL */

.left-panel {
    resize: horizontal;

    min-width: 240px;
    max-width: 500px;

    overflow: hidden;

    display: flex;
    flex-direction: column;

    min-height: 0;
}

.file-structure {
    flex: 1;

    overflow-y: auto;

    padding: 18px;

    min-height: 0;
}

.folder {
    font-weight: 600;
    margin-top: 15px;
}

.nested {
    margin-left: 20px;
    margin-top: 10px;

    color: rgba(255,255,255,0.75);

    word-break: break-word;
}

.empty-state {
    color: rgba(255,255,255,0.45);
}

/* CENTER PANEL */

.center-panel {
    display: flex;
    flex-direction: column;

    overflow: hidden;

    min-height: 0;
}

.hero-section {
    display: flex;
    justify-content: center;
    align-items: center;

    padding: 18px 24px;

    border-bottom: 1px solid rgba(255,255,255,0.05);

    background: rgba(255,255,255,0.02);
}

.hero-input {
    width: 100%;
    max-width: 760px;

    display: flex;
    gap: 14px;
}

.hero-input input {
    flex: 1;

    padding: 16px 18px;

    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 14px;

    background: rgba(255,255,255,0.05);

    color: white;

    outline: none;

    font-size: 14px;
}

.hero-input input::placeholder {
    color: rgba(255,255,255,0.4);
}

.hero-input button {
    padding: 16px 22px;

    border: none;
    border-radius: 14px;

    background: linear-gradient(135deg, #00d4ff, #7b61ff);

    color: white;

    font-weight: 600;

    cursor: pointer;

    transition: 0.3s ease;

    white-space: nowrap;
}

.hero-input button:hover {
    transform: translateY(-2px);

    box-shadow: 0 10px 20px rgba(0,212,255,0.2);
}

/* VISUALIZATION AREA */

.visualization-area {
    flex: 1;

    overflow-y: auto;

    padding: 22px;

    min-height: 0;
}

.welcome-card,
.architecture-card {
    width: 100%;

    background: rgba(255,255,255,0.03);

    border: 1px solid rgba(255,255,255,0.06);

    border-radius: 20px;

    padding: 35px;
}

.welcome-card h2,
.architecture-card h2 {
    margin-bottom: 20px;

    color: #00d4ff;
}

.welcome-card p {
    line-height: 1.8;

    color: rgba(255,255,255,0.75);
}

.flow-box {
    margin: 12px 0;

    padding: 16px;

    border-radius: 14px;

    background: linear-gradient(
        135deg,
        rgba(0,212,255,0.15),
        rgba(123,97,255,0.15)
    );

    border: 1px solid rgba(255,255,255,0.06);
}

.arrow {
    text-align: center;

    font-size: 24px;

    color: #00d4ff;
}

/* RIGHT PANEL */

.right-panel {
    resize: horizontal;

    min-width: 260px;
    max-width: 500px;

    overflow: hidden;

    display: flex;
    flex-direction: column;

    min-height: 0;
}

.insights-container {
    flex: 1;

    overflow-y: auto;

    padding-bottom: 20px;

    min-height: 0;
}

.context-card {
    margin: 20px;

    padding: 18px;

    border-radius: 16px;

    background: rgba(255,255,255,0.04);

    border: 1px solid rgba(255,255,255,0.05);
}

.context-card h3 {
    margin-bottom: 12px;

    color: #00d4ff;
}

.context-card p {
    line-height: 1.8;

    color: rgba(255,255,255,0.78);
}

/* QUERY PANEL */

.query-panel {
    height: 90px;

    display: flex;
    align-items: center;

    gap: 15px;

    padding: 20px;

    border-top: 1px solid rgba(255,255,255,0.06);

    background: rgba(255,255,255,0.03);
}

.query-panel input {
    flex: 1;

    padding: 16px 18px;

    border-radius: 14px;

    border: 1px solid rgba(255,255,255,0.08);

    background: rgba(255,255,255,0.04);

    color: white;

    outline: none;

    font-size: 15px;
}

.query-panel button {
    padding: 16px 22px;

    border: none;
    border-radius: 14px;

    background: linear-gradient(135deg, #00d4ff, #7b61ff);

    color: white;

    font-weight: 600;

    cursor: pointer;
}

/* RESPONSIVE */

@media (max-width: 1200px) {

    body {
        overflow-y: auto;
    }

    .main-layout {
        grid-template-columns: 1fr;
    }

    .hero-input {
        flex-direction: column;
    }

    .hero-section h1 {
        font-size: 32px;
    }

    .query-panel {
        flex-direction: column;
        height: auto;
    }

    .left-panel,
    .right-panel {
        resize: none;
        max-width: 100%;
    }
}

.file-item {
    margin-bottom: 12px;
}

.file-name {
    padding: 8px;
    border-radius: 8px;
    cursor: pointer;
    transition: 0.2s;
}

.file-name:hover {
    background: rgba(255,255,255,0.08);
}

.active-file {
    background: #3b82f6;
    color: white;
}

.function-list {
    margin-left: 18px;
    margin-top: 6px;
}

.function-item {
    padding: 5px 0;
    opacity: 0.85;
    font-size: 14px;
}

.file-item,
.folder-item,
.nested,
.tree-folder,
.tree-file {
    cursor: pointer;
    transition: 0.2s;
}

.file-item:hover,
.folder-item:hover,
.nested:hover,
.tree-folder:hover,
.tree-file:hover {
    background-color: rgba(255,255,255,0.08);
}

/* CUSTOM SCROLLBAR */

::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}

::-webkit-scrollbar-track {
    background: transparent;
}

::-webkit-scrollbar-thumb {
    background: rgba(255,255,255,0.12);
    border-radius: 20px;
}

::-webkit-scrollbar-thumb:hover {
    background: rgba(255,255,255,0.2);
}


script.js:
console.log("WINDOW FULLY LOADED");

window.onbeforeunload = function () {
    console.log("PAGE IS TRYING TO RELOAD");
};

document.addEventListener("submit", (e) => {
    e.preventDefault();
});

window.addEventListener("DOMContentLoaded", () => {

    const analyzeBtn = document.getElementById("analyzeBtn");
    const repoUrlInput = document.getElementById("repoUrl");

    const explorer = document.querySelector(".file-structure");
    const visualizationArea = document.querySelector(".visualization-area");
    const insightsContainer = document.querySelector(".insights-container");
    const askBtn = document.getElementById("askBtn");
    const queryInput = document.getElementById("queryInput");
    let selectedFile = null;

    console.log(analyzeBtn);

    /*
    =========================================
    RENDER TREE
    =========================================
    */

    function renderTree(tree, parentPath = "") {

        let html = "";

        for (const key in tree) {

            const currentPath = parentPath
                ? `${parentPath}/${key}`
                : key;

            const isFolder =
                Object.keys(tree[key]).length > 0;

            if (isFolder) {

                const folderId = currentPath
                    .replaceAll("/", "_");

                html += `
                    <div class="folder">

                        <div
                            class="folder-name"
                            onclick="toggleFolder('${folderId}')"
                        >
                            📁 ${key}
                        </div>

                        <div
                            id="${folderId}"
                            class="folder-content"
                            style="display:none; padding-left:15px;"
                        >
                            ${renderTree(tree[key], currentPath)}
                        </div>

                    </div>
                `;

            } else {

                html += `
                    <div
                        class="nested file-item"
                        onclick="selectFile('${currentPath}')"
                    >
                        📄 ${key}
                    </div>
                `;
            }
        }

        return html;
    }

    /*
    =========================================
    GLOBAL FUNCTIONS
    =========================================
    */

    window.toggleFolder = function(folderId) {

        const folder =
            document.getElementById(folderId);

        if (!folder) return;

        if (folder.style.display === "none") {
            folder.style.display = "block";
        } else {
            folder.style.display = "none";
        }
    };

    window.selectFile = function(filePath) {

        selectedFile = filePath;

        document
            .querySelectorAll(".file-item")
            .forEach(item => {
                item.style.background = "transparent";
            });

        event.target.style.background =
            "rgba(255,255,255,0.1)";

        const currentData =
            window.latestRepositoryData;

        const functions =
            currentData.file_data[filePath] || [];

        let functionsHTML = "";

        functions.forEach(item => {

            functionsHTML += `
                <div class="context-card">

                    <h3>
                        ${item.type.toUpperCase()}
                    </h3>

                    <p>${item.name}</p>

                    <small>
                        Lines:
                        ${item.start_line}
                        -
                        ${item.end_line}
                    </small>

                </div>
            `;
        });

        insightsContainer.innerHTML = `
            <div class="context-card">

                <h3>Selected File</h3>

                <p>${filePath}</p>

            </div>

            ${functionsHTML}
        `;
    };

    /*
    =========================================
    ANALYZE BUTTON
    =========================================
    */

    analyzeBtn.addEventListener("click", async (e) => {

        e.preventDefault();
        e.stopPropagation();

        const repoUrl = repoUrlInput.value.trim();

        if (!repoUrl) {
            alert("Enter repository URL");
            return;
        }

        analyzeBtn.innerText = "Processing...";
        analyzeBtn.disabled = true;

        explorer.innerHTML = `
            <div class="nested">
                Scanning repository...
            </div>
        `;

        try {

            const response = await fetch(
                "http://192.168.56.1:8000/repo/ingest",
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        repo_url: repoUrl
                    })
                }
            );

            const startData = await response.json();

            const jobId = startData.job_id;

            const interval = setInterval(async () => {

                try {

                    const statusResponse = await fetch(
                        `http://192.168.56.1:8000/repo/status/${jobId}`
                    );

                    const data =
                        await statusResponse.json();

                    window.latestRepositoryData = data;

                    /*
                    =========================================
                    RENDER TREE
                    =========================================
                    */

                    explorer.innerHTML =
                        renderTree(data.tree);

                    /*
                    =========================================
                    CENTER PANEL
                    =========================================
                    */

                    visualizationArea.innerHTML = `
                        <div class="architecture-card">

                            <h2>
                                Repository Processing
                            </h2>

                            <div class="flow-box">
                                ${data.status}
                            </div>

                            <div class="arrow">↓</div>

                            <div class="flow-box">
                                ${data.current_file}
                            </div>

                            <div class="arrow">↓</div>

                            <div class="flow-box">
                                ${data.processed_count}
                                /
                                ${data.total_files}
                            </div>

                            <div class="arrow">↓</div>

                            <div class="flow-box">
                                ${data.chunks}
                                chunks stored
                            </div>

                        </div>
                    `;

                    /*
                    =========================================
                    COMPLETED
                    =========================================
                    */

                    if (data.status === "completed") {

                        clearInterval(interval);

                        analyzeBtn.innerText =
                            "Analyze Repository";

                        analyzeBtn.disabled = false;

                        visualizationArea.innerHTML = `
                            <div class="architecture-card">

                                <h2>
                                    Repository Ready
                                </h2>

                                <div class="flow-box">
                                    ${data.total_files}
                                    files indexed
                                </div>

                                <div class="arrow">↓</div>

                                <div class="flow-box">
                                    ${data.chunks}
                                    chunks stored
                                </div>

                                <div class="arrow">↓</div>

                                <div class="flow-box">
                                    Ready for AI querying
                                </div>

                            </div>
                        `;
                    }

                } catch (err) {

                    console.error(err);

                }

            }, 1500);

        } catch (err) {

            console.error(err);

            analyzeBtn.innerText =
                "Analyze Repository";

            analyzeBtn.disabled = false;
        }

    });



/*
=========================================
ASK AI
=========================================
*/

askBtn.addEventListener("click", async () => {

    const query = queryInput.value.trim();

    if (!query) {
        alert("Enter a query");
        return;
    }

    visualizationArea.innerHTML = `
        <div class="architecture-card">

            <h2>Thinking...</h2>

            <div class="flow-box">
                Retrieving repository context
            </div>

            <div class="arrow">↓</div>

            <div class="flow-box">
                Generating AI explanation
            </div>

        </div>
    `;

    try {

        const response = await fetch(
            "http://192.168.56.1:8000/query/ask",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    query: query
                })
            }
        );

        const data = await response.json();

        visualizationArea.innerHTML = `
            <div class="architecture-card">

                <h2>AI Repository Explanation</h2>

                <div class="context-card">

                    <h3>Question</h3>

                    <p>${data.query}</p>

                </div>

                <div class="context-card">

                    <h3>AI Answer</h3>

                    <p style="white-space: pre-wrap;">
                        ${data.answer}
                    </p>

                </div>

            </div>
        `;

    } catch (err) {

        console.error(err);

        visualizationArea.innerHTML = `
            <div class="architecture-card">

                <h2 style="color:red;">
                    Query Failed
                </h2>

                <p>${err.message}</p>

            </div>
        `;
    }

});

});