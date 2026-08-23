import pytest
from clients.github_client import GithubClient

@pytest.fixture
def github():
    return GithubClient()

@pytest.fixture
def temp_repo(github):
    response = github.create_repo("test-repo-fixture")
    assert response.status_code == 201
    name = response.json()["name"]
    try:
        yield name
    finally:
        github.delete_repo(name)