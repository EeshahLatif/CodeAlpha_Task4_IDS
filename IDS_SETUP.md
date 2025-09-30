# IDS Setup Guide (Snort) — CodeAlpha Task 4

## 📌 Install Snort (Ubuntu / Linux)
Run these commands in a Linux terminal one by one:

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Snort
sudo apt install snort -y

# Verify installation
snort -V
