<div align="center">
  <h2 align="center">Spotify Client Version Checker</h2>
  <p align="center">
    A simple script that tracks Spotify Web Player, Android, and iOS client versions by checking them every 10 minutes.
  </p>
</div>

---

### ⚙️ Installation

- Requires: Python 3.x
- Install dependencies: `pip install requests`

### 📝 Usage

The script automatically runs every hour via GitHub Actions. It:

1. Fetches the Spotify Web Player page for the web client version
2. Checks the App Store for iOS version
3. Checks AppBrain for Android version
4. Updates respective version files if any version has changed:
   - version.txt (Web Player)
   - ios_version.txt (iOS)
   - android_version.txt (Android)

To run manually:

```bash
python main.py
```

### 📜 ChangeLog

```diff
v0.0.2 ⋮ 2024
+ Added Android and iOS version tracking

v0.0.1 ⋮ 2024
! Initial release with automatic version checking
```

# Spotify Client Version Tracker

![Web Version](https://img.shields.io/badge/Spotify%20Web-1.2.59.145.g1554f747-brightgreen)
![iOS Version](https://img.shields.io/badge/Spotify%20iOS-8.8.22-blue)
![Android Version](https://img.shields.io/badge/Spotify%20Android-8.8.22.510-orange)

Last checked: 2025-02-26 10:53 UTC

## Latest Check Status

- **Web Version**: `1.2.59.137.g41d5398d`
- **iOS Version**: `8.8.22`
- **Android Version**: `8.8.22.510`
- **Last Updated**: 2025-02-26 09:57 UTC
- **Status**: Active
