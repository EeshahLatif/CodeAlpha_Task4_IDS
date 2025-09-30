# Task 4 - Network Intrusion Detection System (IDS) Report

## What I implemented
- Added a Snort rule (`local.rules`) to detect ICMP ping packets.
- Created a Python IDS demo (`python_ids_demo.py`) that listens for ICMP packets and prints alerts.
- Wrote installation and run instructions for Snort (`IDS_SETUP.md`) and demo instructions (`run_demo_instructions.txt`).

## Why this matters
- ICMP ping detection can reveal scanning or reconnaissance attempts.
- Writing rules is the foundation of IDS operation.
- The Python demo shows live alerts without needing Snort installed.

## Evidence
- `screenshots/demo_alert.png` shows demo alerts.
- Snort (if installed) also prints alerts in console.

## Next steps
- Run Snort/Suricata on a Linux VM.
- Forward Snort logs to a SIEM and visualize with Kibana/Grafana.
