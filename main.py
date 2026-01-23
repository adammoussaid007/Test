import base64
import requests

# ===============================
# CONFIGURATION
# ===============================
GITHUB_TOKEN = "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"  # replace with your GitHub PAT
REPO_OWNER = "adammoussaid007"               # GitHub username or org
REPO_NAME = "Test"                    # repository name
FILE_PATH_IN_REPO = "accounts.json" # path in the repo
LOCAL_FILE_PATH = "accounts.json"           # local file to upload
COMMIT_MESSAGE = "Add/update file via API"

# ===============================
# STEP 1: Read local file and encode
# ===============================
with open(LOCAL_FILE_PATH, "rb") as f:
    content = f.read()

# Base64 encode content
b64_content = base64.b64encode(content).decode("utf-8")

# ===============================
# STEP 2: Check if file exists (to decide create/update)
# ===============================
url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{FILE_PATH_IN_REPO}"
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    # File exists → we need its SHA to update
    sha = response.json()["sha"]
    print(f"File exists, updating. SHA: {sha}")
else:
    # File does not exist → create
    sha = None
    print("File does not exist, creating.")

# ===============================
# STEP 3: Upload file (create/update)
# ===============================
data = {
    "message": COMMIT_MESSAGE,
    "content": b64_content
}

if sha:
    data["sha"] = sha

upload_response = requests.put(url, headers=headers, json=data)

if upload_response.status_code in [200, 201]:
    print("File uploaded successfully!")
    print(upload_response.json()["content"]["html_url"])
else:
    print("Failed to upload file")
    print(upload_response.status_code, upload_response.text)
