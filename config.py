from dotenv import load_dotenv
load_dotenv()  # reads .env from project root, loads into env
import os

BASE_URI = "https://api.github.com"
TOKEN = os.getenv("GITHUB_TOKEN")
HEADERS = {"Authorization": f"Bearer {TOKEN}", "Accept": "application/vnd.github+json"}
BAD_HEADERS = {"Authorization": "Bearer fake_token_lol", "Accept": "application/vnd.github+json"}
OWNER = "justxki"
REPO_NAME = "test-playground"
REPO_URI = f"{BASE_URI}/repos/{OWNER}/{REPO_NAME}" # https://api.github.com/repos/justxki/test-playground
ISSUES_URI = f"{REPO_URI}/issues" # https://api.github.com/repos/justxki/test-playground/issues
USER_URI = f"{BASE_URI}/user" # https://api.github.com/user
USER_REPOS_URI = f"{USER_URI}/repos" # https://api.github.com/user/repos