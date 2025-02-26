import requests
import re

def get_script_link():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    }

    response = requests.get('https://open.spotify.com/intl-fr/', headers=headers)
    
    # Look for the web-player script URL
    script_pattern = r'src="(https://open\.spotifycdn\.com/cdn/build/web-player/web-player\.[a-f0-9]+\.js)"'
    script_match = re.search(script_pattern, response.text)
    
    if script_match:
        return script_match.group(1)
    return None

def get_version(url):
    headers = {
        'accept': '*/*',
    }

    response = requests.get(url, headers=headers)

    # Look for clientVersion pattern
    version_pattern = r'clientVersion:"([\d\.]+g[a-f0-9]+)"'
    version_match = re.search(version_pattern, response.text)

    if version_match:
        version = version_match.group(1)
        return version
    else:
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
script_url = get_script_link()
ios_version = get_ios_version()

with open("ios_version.txt", "w") as ios_file:
    ios_file.write(ios_version)

with open("android_version.txt", "w") as android_file:
    android_file.write(android_version)

if script_url:
    version = get_version(script_url)
    with open("version.txt", "w") as f:
        f.write(version)
