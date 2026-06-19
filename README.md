<!-- SPONSOR-START -->
---

<div align="center">

### 🌐 Need Proxies? Check out my services

<a href="https://vaultproxies.com" target="_blank" rel="noopener noreferrer">
  <img src="https://i.imgur.com/TF165pP.gif" alt="VaultProxies">
</a>
<p></p>

<table>
  <tr>
    <th>Service</th>
    <th>Pricing</th>
    <th>Features</th>
  </tr>
  <tr>
    <td><b><a href="https://vaultproxies.com" target="_blank" rel="noopener noreferrer">🔮 VaultProxies</a></b></td>
    <td><code>$1.00/GB</code> residential</td>
    <td>Residential · IPv6 · Residential Unlimited · Datacenter</td>
  </tr>
  <tr>
    <td><b><a href="https://nullproxies.com" target="_blank" rel="noopener noreferrer">🌑 NullProxies</a></b></td>
    <td><code>$0.75/GB</code> residential</td>
    <td>Residential · Residential Unlimited · DC Unlimited · Mobile Proxies</td>
  </tr>
  <tr>
    <td><b><a href="https://strikeproxy.net" target="_blank" rel="noopener noreferrer">⚡ StrikeProxy</a></b></td>
    <td><code>$0.75/GB</code> residential</td>
    <td>Residential · Residential Unlimited · DC Unlimited · Mobile Proxies</td>
  </tr>
</table>
</div>

<!-- SPONSOR-END -->

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

![Web Version](https://img.shields.io/badge/Spotify%20Web-1.2.93.403.g62ff9508-brightgreen)
![iOS Version](https://img.shields.io/badge/Spotify%20iOS-9.1.56-blue)
![Android Version](https://img.shields.io/badge/Spotify%20Android-9.1.56.574-orange)

Last checked: 2026-06-19 00:11 UTC
