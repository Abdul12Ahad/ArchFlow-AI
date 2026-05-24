import os
from git import Repo

REPO_BASE_PATH = "E:/AI_TEMP_REPOS"

def clone_repository(repo_url: str):

    repo_name = repo_url.split("/")[-1].replace(".git","")

    local_path = os.path.join(REPO_BASE_PATH, repo_name)

    if os.path.exists(local_path):
        return local_path
    
    Repo.clone_from(repo_url, local_path)

    return local_path