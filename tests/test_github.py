
from config import OWNER

def test_create_issue(github):
    response = github.create_issue("Test Title Name")
    assert response.status_code == 201
    assert response.json()["title"] == "Test Title Name"
    assert response.json()["state"] == "open"
    assert response.json()["number"] > 0

def test_close_issue(github):
    response = github.create_issue("Test Title Name")
    ticket_num = response.json()["number"]
    response2 = github.close_issue(ticket_num)
    assert response2.status_code == 200
    assert response2.json()["state"] == "closed"

def test_list_issues(github):
    response = github.list_issues()
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_issue(github):
    response1 = github.create_issue("Issue Title")
    issue_number = response1.json()["number"]
    response2 = github.get_issue(issue_number)
    assert response2.status_code == 200
    assert response2.json()["number"] == issue_number
    assert response2.json()["title"] == "Issue Title"

def test_get_repo(github, temp_repo):
    response = github.get_repo(temp_repo)
    assert response.status_code == 200
    assert response.json()["name"] == temp_repo

def test_create_repo(github):
    response = github.create_repo("test-repo-create-8-17")
    assert response.status_code == 201
    assert response.json()["name"] == "test-repo-create-8-17"

def test_list_repos(github):
    response = github.list_repos()
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_delete_repo(github):
    response1 = github.create_repo("test-repo-delete-8-17")
    repo_name = response1.json()["name"]
    response2 = github.delete_repo(repo_name)
    assert response2.status_code == 204
    assert repo_name not in [repo["name"] for repo in github.list_repos().json()]

def test_get_authenticated_user(github):
    response = github.get_authenticated_user()
    assert response.status_code == 200
    assert response.json()["login"] == OWNER

def test_error_create_dupe_repo(github, temp_repo):
    response = github.create_repo(temp_repo)
    assert response.status_code == 422
    assert "name already exists" in response.json()["errors"][0]["message"]