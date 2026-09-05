# Simple TCP Port Scanner

A lightweight, zero-dependency Python tool designed for rapid scanning of common TCP network ports on target IPv4 addresses or hostnames using standard socket connections.

---

## Key Features

* **Zero Third-Party Dependencies:** Implemented entirely with Python's native `socket` module.
* **Domain & IPv4 Resolution:** Accepts both domain names (e.g., `example.com`) and direct IP addresses, resolving targets dynamically with `socket.gethostbyname`.
* **Targeted Port Suite:** Scans 11 essential services out of the box (FTP, SSH, Telnet, SMTP, DNS, HTTP, POP3, IMAP, HTTPS, MySQL, and HTTP-Proxy).
* **Timeout-Controlled Scanning:** Uses a non-blocking `1.0s` connection timeout per port to avoid hanging on non-responsive or firewalled hosts.
* **CLI Status Formatting:** Displays aligned output with clear `[+] OPEN` and `[-] CLOSED` status indicators alongside protocol labels.
* **Signal & Exception Handling:** Safely captures keyboard interrupts (`Ctrl+C`), DNS resolution failures (`socket.gaierror`), and unhandled runtime exceptions.

---

## Project Structure

```text
.
├── scanner.py      # Main Python port scanner script
└── README.md       # Project documentation
```

---

## Technical Overview

The underlying script uses Python's `socket.SOCK_STREAM` interface to initiate a standard TCP three-way handshake (`SYN` -> `SYN-ACK` -> `ACK`) with target ports via `connect_ex()`. 

Unlike `connect()`, which raises an exception on connection failure, `connect_ex()` returns an explicit error code integer:
* `0`: Connection succeeded (Port is **OPEN**).
* `111` / `10061` / `Timeout`: Connection refused or dropped (Port is **CLOSED** or **FILTERED**).

---

## Usage Guide

### Requirements
* Python **3.6+** (No external package installation required)

### Running the Scanner

1. **Clone the repository:**
   ```bash
   git clone https://github.com/void-syntax/tcp-port-scanner.git
   cd tcp-port-scanner
   ```

2. **Execute the script:**
   ```bash
   python3 scanner.py
   ```

3. **Sample Terminal Output:**
   ```text
   Enter IP address or domain: scanme.nmap.org

   [+] Scanning: scanme.nmap.org (45.33.32.156)
   ---------------------------------------------
   [-] Port 21    (FTP       ) : CLOSED
   [+] Port 22    (SSH       ) : OPEN
   [-] Port 23    (Telnet    ) : CLOSED
   [-] Port 25    (SMTP      ) : CLOSED
   [-] Port 53    (DNS       ) : CLOSED
   [+] Port 80    (HTTP      ) : OPEN
   [-] Port 110   (POP3      ) : CLOSED
   [-] Port 143   (IMAP      ) : CLOSED
   [+] Port 443   (HTTPS     ) : OPEN
   [-] Port 3306  (MySQL     ) : CLOSED
   [-] Port 8080  (HTTP-Proxy) : CLOSED
   ---------------------------------------------
   Total open ports found: 3
   Scanning complete.
   ```

---

## Roadmap & Future Enhancements

* [ ] Add multi-threading support using `concurrent.futures` to speed up sequential socket attempts.
* [ ] Allow custom port range input via CLI command-line arguments (`argparse`).
* [ ] Implement banner grabbing to detect service versions running on open ports.
* [ ] Add JSON output export for integration with other diagnostic pipelines.

---

## Legal & Security Disclaimer

This project is intended strictly for educational purposes, security testing within authorized environments, and local network management. Executing port scans against hosts without explicit permission may violate local computing regulations, internet service provider terms of service, and applicable network privacy laws. Always ensure you have express authorization before targeting external hosts.
