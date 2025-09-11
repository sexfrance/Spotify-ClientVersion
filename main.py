import requests
import re

def get_client_version_from_html():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    }
    response = requests.get('https://open.spotify.com/intl-fr/', headers=headers)
    match = re.search(r'<script id="appServerConfig" type="text/plain">(.*?)</script>', response.text)
    if match:
        import base64
        import json
        b64 = match.group(1).strip()
        try:
            decoded = base64.b64decode(b64 + "==")
        except Exception:
            decoded = base64.b64decode(b64)
        try:
            # Try to decode as utf-8 and parse JSON
            data = json.loads(decoded.decode('utf-8'))
            return data.get('clientVersion', 'Version not found')
        except Exception:
            return "Version not found"
    return "Version not found"

def get_ios_version(app_id: str = "324684580") -> str:
    url = f"https://itunes.apple.com/lookup?id={app_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'results' in data and len(data['results']) > 0:
            return data['results'][0].get('version', 'Unknown')
    return 'Unknown'

def get_android_version():
    url = f"https://www.appbrain.com/app/spotify-music-and-podcasts/com.spotify.music"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        match = re.search(r'<meta itemprop="softwareVersion" content="([0-9.]+)"', response.text)
        if match:
            return match.group(1)
    return 'Unknown'


android_version = get_android_version()
ios_version = get_ios_version()
website_version = get_client_version_from_html()

with open("ios_version.txt", "w") as ios_file:
    ios_file.write(ios_version)

with open("android_version.txt", "w") as android_file:
    android_file.write(android_version)

with open("version.txt", "w") as f:
    f.write(website_version)
