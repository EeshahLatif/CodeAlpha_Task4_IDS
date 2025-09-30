python_ids_demo.py
Simple IDS demo for CodeAlpha Task 4.
Detects ICMP (ping) packets and prints ALERT messages.

Requirements:
- Python 3
- scapy (recommended) -> pip install scapy
Run as Administrator/root for packet capture:
- Windows: run Python or PyCharm as Administrator
- Linux/Mac: run with sudo
"""

import sys

try:
    from scapy.all import sniff, ICMP, IP
    USE_SCAPY = True
except Exception:
    USE_SCAPY = False

def scapy_callback(pkt):
    if IP in pkt and ICMP in pkt:
        src = pkt[IP].src
        dst = pkt[IP].dst
        print(f"[ALERT] ICMP Ping Detected | src={src} -> dst={dst}")

def run_with_scapy():
    print("🚀 IDS Demo started (scapy). Listening for ICMP traffic...")
    print("Press Ctrl+C to stop.")
    sniff(filter="icmp", prn=scapy_callback)

def run_socket_fallback():
    import socket
    print("Scapy not found. Running minimal socket fallback (may be limited).")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    except PermissionError:
        print("Permission error: run this script as Administrator/root.")
        sys.exit(1)
    except Exception as e:
        print("Socket error:", e)
        sys.exit(1)

    print("Socket fallback running. Listening for ICMP packets...")
    try:
        while True:
            data, addr = s.recvfrom(65535)
            print(f"[ALERT] ICMP-like packet detected from {addr[0]}")
    except KeyboardInterrupt:
        print("\nStopped by user.")

if __name__ == "__main__":
    if USE_SCAPY:
        try:
            run_with_scapy()
        except KeyboardInterrupt:
            print("\nStopped by user.")
        except Exception as e:
            print("Scapy capture error:", e)
            print("Install scapy with: pip install scapy")
    else:
        print("Scapy not installed. Install with: pip install scapy")
        run_socket_fallback()
