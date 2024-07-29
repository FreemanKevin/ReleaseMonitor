import requests
import json
import os

# 从环境变量中获取个人访问令牌
access_token = os.getenv('getRepo')

def get_releases(owner, repo, access_token):
    url = f"https://api.github.com/repos/{owner}/{repo}/releases"
    headers = {'Authorization': f'token {access_token}'}
    response = requests.get(url, headers=headers)
    releases_data = response.json() if response.ok else []
    
    # 提取每个发布的版本号和发布日期
    releases = []
    for release in releases_data:
        release_info = {
            'tag_name': release.get('tag_name'),  # 版本号
            'published_at': release.get('published_at')  # 发布日期
        }
        releases.append(release_info)
    
    return releases

def save_releases(releases, filename):
    directory = "data"
    if not os.path.exists(directory):
        os.makedirs(directory)
    filepath = os.path.join(directory, filename)
    with open(filepath, 'w') as file:
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
    releases = get_releases(owner, repo, access_token)
    filename = f"{repo}_releases.json"
    save_releases(releases, filename)