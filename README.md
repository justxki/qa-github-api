# qa-github-api

QA automation suite for [GitHub's public API](https://docs.github.com/en/rest) using pytest and requests. Covers issue and repo CRUD operations plus negative cases.

## Setup

#### 1. Clone the repo and cd into it:

git clone https://github.com/justxki/qa-github-api.git
cd qa-github-api

#### 2. Create and activate a virtual environment:

python -m venv .venv
.venv\Scripts\activate # windows
source .venv/bin/activate # mac/linux

#### 3. Install dependencies:

pip install -r requirements.txt

#### 4. Create a `.env` file in the project root with your GitHub credentials:

GITHUB_TOKEN=your_github_token_here

   - Get your Token from [GitHub profile settings](https://github.com/settings/apps).
     - Click on 'Personal Access Tokens' (Specifically, 'Fine-grained personal access token')
       - For Fine-grained tokens: "Grant permissions: Repository access → All repositories (or specific), Repository permissions → Contents: Read/Write, Issues: Read/Write."


## Running tests

From the project root:

pytest # run all tests
pytest -v # verbose output
pytest tests/test_github.py::test_create_issue # single test


## Project structure

```
qa-github-api/
├── client/
│   └── github_client.py       # GithubClient — wraps requests to GitHub endpoints
├── tests/
│   ├── conftest.py                             # shared fixtures (temp_repo)
│   ├── test_github.py                          # test suite
│   ├── test_first_practice_github.py           # isolated api testing
│   └── test_second_practice_github.py         # isolated api testing
├── config.py                # env vars, headers, URIs
├── requirements.txt
└── .env                     # credentials (gitignored)
```

## Coverage

- Create a new issue
- Close an issue
- List all issues
- Get an issue
- Get a repo
- Create a new repo
- List all repos
- Delete a repo
- Get an authenticated user
- Create a repo that already exists (negative)

## API quirks documented during testing

- 404 for both nonexistent AND private repos — github doesn't distinguish between "doesn't exist" and "exists but you can't see it" for security reasons. If you tested this, worth noting.
- DELETE repo returns 204 (no content), not 200 or 202 — some APIs return 200 with a success message, github returns 204 empty. Worth noting if it surprised you.
- 422 for duplicate repo name — you have a test for this. 422 = "semantically wrong" not 400 = "malformed." Worth noting the distinction.
- Rate limits are aggressive on write endpoints — did you hit any 429s during dev? If yes, mention.
- Closing an issue uses PATCH /repos/{owner}/{repo}/issues/{issue_number} with state: "closed" in the body — not DELETE. A closed issue still exists in a "closed" state. GitHub's REST API doesn't support issue deletion at all (only open/close/edit); deletion is available only via GitHub's GraphQL API or the web UI.
