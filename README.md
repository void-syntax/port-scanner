# Simple Python Port Scanner

A lightweight and easy-to-understand TCP port scanner written in Python using only standard libraries. Designed for basic network reconnaissance and learning socket programming fundamentals.

## Features

- **Zero dependencies:** Uses Python's built-in `socket` module.
- **Common port coverage:** Scans default service ports (21, 22, 80, 443, 8080, etc.).
- **Domain resolution:** Accepts both IP addresses (`192.168.1.1`) and domain names (`scanme.nmap.org`).
- **Graceful interruption:** Handles `Ctrl+C` to exit cleanly without throwing unhandled tracebacks.

## Prerequisites

- Python 3.x

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/void-syntax/port-scanner.git
   cd port-scanner
Run the script:

Bash
python scanner.py
Enter the target IP or domain name when prompted.

Author
## GitHub: @void-syntax

## Disclaimer
This tool is created for educational and authorized testing purposes only. Scanning targets without explicit permission is illegal in many jurisdictions. Always obtain proper authorization before scanning any network or system.
