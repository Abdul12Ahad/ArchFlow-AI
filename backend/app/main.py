from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

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

app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

@app.get("/")
def home():
    return {"message": "AI Codebase Explainer Backend Running"}