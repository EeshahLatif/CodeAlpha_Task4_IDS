# IDS Setup Guide (Snort) — CodeAlpha Task 4

> This guide shows the basic steps to install and run Snort on a Linux system (Ubuntu).  
> If you are on Windows, see Snort docs for Windows installation. This repo also contains a Python demo you can run locally.

## Install Snort (Ubuntu example)
1. Update system:
   ```bash
   sudo apt update && sudo apt upgrade -y
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

bash
Copy code
sudo nano /etc/snort/rules/local.rules
Paste this rule inside:

python
Copy code
alert icmp any any -> any any (msg:"ICMP Ping Detected - CodeAlpha Task4"; sid:1000001; rev:1;)
Save and exit (CTRL + O, Enter, CTRL + X).

📌 Run Snort with Rules
Start Snort in console mode (replace eth0 with your network interface, e.g., wlan0 for WiFi):

bash
Copy code
sudo snort -A console -q -c /etc/snort/snort.conf -i eth0
📌 Test the IDS
Open another terminal and send a ping:

bash
Copy code
ping 127.0.0.1 -c 4
You should see alerts like:

css
Copy code
[**] [1:1000001:1] ICMP Ping Detected - CodeAlpha Task4 [**]
