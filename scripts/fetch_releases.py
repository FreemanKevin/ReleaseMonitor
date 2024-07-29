import requests
import json
import os

# 从环境变量中获取个人访问令牌
access_token = os.getenv('getRepo')  

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

def save_releases(releases, filename):
    directory = "data"
    if not os.path.exists(directory):
        os.makedirs(directory)
    filepath = os.path.join(directory, filename)
    with open(filepath, 'w') as file:
        json.dump(releases, file, indent=4)
    print(f"Saved data to {filepath}")  # Debug: 显示保存文件的路径

# 只针对 minio 项目进行操作
owner = "minio"
repo = "minio"
releases = get_releases(owner, repo, access_token)
filename = f"{repo}_releases.json"
save_releases(releases, filename)