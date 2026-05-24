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

mermaid.init(undefined, document.querySelectorAll(".mermaid"));

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
        let sourceHTML = "";

        if (data.sources) {

        data.sources.forEach(source => {

            sourceHTML += `

                <div class="snippet-card">

                    <div class="snippet-header">

                        <div>
                            <strong>${source.function}</strong>
                        </div>

                        <div class="snippet-file">
                            ${source.file}
                        </div>

                    </div>

                    <div class="snippet-type">
                        ${source.type}
                        •
                        ${source.language}
                    </div>

                    <pre class="code-block"><code>${source.code}</code></pre>
                </div>
            `;
        });

        }

        visualizationArea.innerHTML = `

        <div class="architecture-card">

        <h2>Repository Architecture</h2>

        <div class="mermaid diagram-box">
            ${data.diagram}
        </div>

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

        <div class="context-card">

            <h3>Relevant Code Snippets</h3>

            ${sourceHTML}

        </div>

        </div>
        `;


mermaid.init(undefined, document.querySelectorAll(".mermaid"));


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