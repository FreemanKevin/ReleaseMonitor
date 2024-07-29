import requests
import json

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

# 假设你的个人访问令牌存储在一个变量中
access_token = 'getRepo'

for project in projects:
    owner = project['owner']
    repo = project['repo']
    releases = get_releases(owner, repo, access_token)
    save_releases(releases, f"{repo}_releases.json")