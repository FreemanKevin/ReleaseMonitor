import requests
import json

def get_releases(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/releases"
    response = requests.get(url)
    releases = response.json() if response.ok else []
    return releases

def save_releases(releases, filename):
    with open(filename, 'w') as file:
        json.dump(releases, file, indent=4)

# 配置需要追踪的项目
projects = [
    {"owner": "alibaba", "repo": "nacos"},
    {"owner": "redis", "repo": "redis"},
    {"owner": "rabbitmq", "repo": "rabbitmq-server"},
    {"owner": "nginx", "repo": "nginx"},
    {"owner": "kekingcn", "repo": "kkFileView"},
    {"owner": "elastic", "repo": "elasticsearch"},
    {"owner": "minio", "repo": "minio"}
]

for project in projects:
    owner = project['owner']
    repo = project['repo']
    releases = get_releases(owner, repo)
    save_releases(releases, f"{repo}_releases.json")