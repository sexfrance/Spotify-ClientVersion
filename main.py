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

script_url = get_script_link()

if script_url:
    version = get_version(script_url)
    with open("version.txt", "w") as f:
        f.write(version)
