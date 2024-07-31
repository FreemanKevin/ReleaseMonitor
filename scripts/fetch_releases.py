import requests
import json
import os

# 从环境变量中获取个人访问令牌
access_token = os.getenv('ACCESS_TOKEN')

def get_releases(owner, repo, access_token):
    url = f"https://api.github.com/repos/{owner}/{repo}/releases"
    headers = {'Authorization': f'token {access_token}'}
    print(f"Fetching releases from {url}")  # Debug: 显示请求的 URL
    response = requests.get(url, headers=headers)
    
    if response.ok:
        releases_data = response.json()
    else:
        print(f"Failed to fetch data: {response.status_code} {response.text}")  # Debug: 显示错误信息
        releases_data = []
    
    # 提取每个发布的版本号和发布日期
    releases = []
    for release in releases_data:
        release_info = {
            'tag_name': release.get('tag_name'),  # 版本号
            'published_at': release.get('published_at')  # 发布日期
        }
        releases.append(release_info)
    
    return releases

def get_tags(owner, repo, access_token):
    url = f"https://api.github.com/repos/{owner}/{repo}/tags"
    headers = {'Authorization': f'token {access_token}'}
    print(f"Fetching tags from {url}")  # Debug: 显示请求的 URL
    response = requests.get(url, headers=headers)
    
    if response.ok:
        tags_data = response.json()
    else:
        print(f"Failed to fetch data: {response.status_code} {response.text}")  # Debug: 显示错误信息
        tags_data = []
    
    # 提取每个 tag 的名称和发布时间
    tags = []
    for tag in tags_data:
        commit_url = tag['commit']['url']
        commit_response = requests.get(commit_url, headers=headers)
        if commit_response.ok:
            commit_data = commit_response.json()
            commit_date = commit_data['commit']['committer']['date']
        else:
            commit_date = "Unknown"
        
        tag_info = {
            'name': tag['name'],
            'date': commit_date
        }
        tags.append(tag_info)
    
    return tags

def save_data(data, filename):
    directory = "data"
    if not os.path.exists(directory):
        os.makedirs(directory)
    filepath = os.path.join(directory, filename)
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Saved data to {filepath}")  # Debug: 显示保存文件的路径

# 配置要获取信息的仓库列表
repositories = [
    ("kekingcn", "kkFileView"),
    ("elastic", "elasticsearch"),
    ("alibaba", "nacos"),
    ("redis", "redis"),
    ("rabbitmq", "rabbitmq-server"),
    ("minio", "minio"),
    ("nginx", "nginx"),
    ("docker", "compose"),
    ("moby", "moby"),
    ("kubernetes", "kubernetes"),
    ("goharbor", "harbor"),
]

# 遍历列表，获取每个仓库的发布信息或标签并保存
for owner, repo in repositories:
    if repo == "nginx":
        tags = get_tags(owner, repo, access_token)
        filename = f"{repo}_tags.json"
        save_data(tags, filename)
    else:
        releases = get_releases(owner, repo, access_token)
        filename = f"{repo}_releases.json"
        save_data(releases, filename)