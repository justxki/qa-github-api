import requests
from config import HEADERS, ISSUES_URI, USER_REPOS_URI, BASE_URI, OWNER


class GithubClient:

    def __init__(self):
        self.headers = HEADERS
        self.issues_uri = ISSUES_URI
        self.user_repos_uri = USER_REPOS_URI
        self.base_uri = BASE_URI


    def create_issue(self, title):
        payload = {"title": title}
        response = requests.post(self.issues_uri, headers=self.headers, json=payload)
        return response

    def close_issue(self, issue_number):
        payload = {"state": "closed"}
        response = requests.patch(f"{self.issues_uri}/{issue_number}", headers=self.headers, json=payload)
        return response


    def list_issues(self):
        response = requests.get(f"{self.issues_uri}", headers=self.headers)
        return response

    def get_issue(self, issue_number):
        response = requests.get(f"{self.issues_uri}/{issue_number}", headers=self.headers)
        return response

    def get_repo(self, name):
        response = requests.get(f"{self.base_uri}/repos/{OWNER}/{name}", headers=self.headers)
        return response

    def create_repo(self, name):
        payload = {"name": name}
        response = requests.post(self.user_repos_uri, headers=self.headers, json=payload)
        return response

    def list_repos(self):
        response = requests.get(self.user_repos_uri, headers=self.headers)
        return response

    def delete_repo(self, name):
        response = requests.delete(f"{self.base_uri}/repos/{OWNER}/{name}", headers=self.headers)
        return response

    def get_authenticated_user(self):
        response = requests.get(f"{self.base_uri}/user", headers=self.headers)
        return response



