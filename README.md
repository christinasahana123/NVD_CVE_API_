# CVE API Project

This Python project fetches CVE (Common Vulnerabilities and Exposures) data from the NVD API and stores it in a local SQLite database. It also provides a Flask-based REST API to query CVEs by ID or by last modified date.

## Features
- Fetches CVE data using NVD API (v2.0)
- Stores in SQLite
- REST API endpoints:
  - `/cve/<cve_id>`
  - `/cves/modified?days=N`

## How to Run
```bash
python main.py     # to fetch and store CVEs
python api.py      # to run the Flask API
