<div align="center">
  <h2 align="center">Spotify Client Version Checker</h2>
  <p align="center">
    A simple script that tracks Spotify Web Player's client version by checking it every hour.
  </p>
</div>

---

### ⚙️ Installation

- Requires: Python 3.x
- Install dependencies: `pip install requests`

### 📝 Usage

The script automatically runs every hour via GitHub Actions. It:

1. Fetches the Spotify Web Player page
2. Extracts the current client version
3. Updates version.txt if the version has changed

To run manually:

```bash
python main.py
```

### 📜 ChangeLog

```diff
v0.0.1 ⋮ 2024
! Initial release with automatic version checking
```

# Spotify Client Version Tracker

![Version](https://img.shields.io/badge/Spotify%20Version-1.2.59.135.g8adc6368-brightgreen)

Last checked: 2025-02-26 03:53 UTC

## Latest Check Status
- **Current Version**: `1.2.59.134.g0e17332f`
- **Last Updated**: <auto-update>
- **Status**: ✅ Active

## About
Automatically tracks Spotify desktop client version changes.
```
