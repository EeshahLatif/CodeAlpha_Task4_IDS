IDS_SETUP.md
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

📌 Add Custom Rule

Edit the local rules file:

sudo nano /etc/snort/rules/local.rules


Paste this rule inside:

alert icmp any any -> any any (msg:"ICMP Ping Detected - CodeAlpha Task4"; sid:1000001; rev:1;)


Save and exit (CTRL + O, Enter, CTRL + X).

📌 Ensure snort.conf includes local.rules

Check snort.conf and confirm it has:

var RULE_PATH /etc/snort/rules
include $RULE_PATH/local.rules

📌 Run Snort with Rules

Start Snort in console mode (replace eth0 with your network interface, e.g., wlan0 for WiFi):

sudo snort -A console -q -c /etc/snort/snort.conf -i eth0

📌 Test the IDS

Open another terminal and send a ping:

ping 127.0.0.1 -c 4


You should see alerts like:

[**] [1:1000001:1] ICMP Ping Detected - CodeAlpha Task4 [**]


✅ This confirms your Snort IDS is working and detecting ICMP traffic.

Notes

Snort is easiest to install on Ubuntu/Linux.

Windows requires extra setup (Npcap + config).
