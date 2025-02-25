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
