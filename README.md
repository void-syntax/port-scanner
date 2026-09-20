<div align="center">

# 🔍 Simple TCP Port Scanner

**A lightweight, zero-dependency Python utility for rapid network reconnaissance and socket testing.**

[![Python](https://img.shields.io/badge/Python-3.6%2B-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![Dependencies](https://img.shields.io/badge/Dependencies-Zero-success?style=for-the-badge)](#key-features)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey?style=for-the-badge)](#requirements)
[![Code Style](https://img.shields.io/badge/Code%20Style-PEP8-brightgreen?style=for-the-badge)](https://peps.python.org/pep-0008/)

[Features](#key-features) • [Installation](#usage-guide) • [Technical Overview](#technical-overview) • [Roadmap](#roadmap--future-enhancements) • [License](#license)

</div>

---

## ⚡ Key Features

* 📦 **Zero External Dependencies:** Built entirely using Python standard libraries (`socket`, `sys`). No `pip install` required.
* 🌐 **Smart Domain & IPv4 Resolution:** Automatically resolves hostnames (e.g., `scanme.nmap.org`) to IPv4 using `socket.gethostbyname`.
* 🎯 **Targeted Service Audit:** Scans 11 high-priority TCP ports by default (FTP, SSH, Telnet, SMTP, DNS, HTTP, POP3, IMAP, HTTPS, MySQL, HTTP-Proxy).
* ⏱️ **Non-Blocking Timeouts:** Implements a strict `1.0s` connection timeout per socket to prevent hanging on firewalled (`DROP`) or unresponsive hosts.
* 🖥️ **Clean CLI Visuals:** Formatted stdout with dynamically aligned columns and intuitive status indicators (`[+] OPEN` / `[-] CLOSED`).
* 🛡️ **Robust Exception Handling:** Gracefully handles keyboard interrupts (`Ctrl+C`), unresolvable hostnames (`socket.gaierror`), and unexpected network errors without crashing.

---

## 📁 Project Structure

```text
.
├── .gitignore          # Git ignore rules
├── LICENSE             # Open-source MIT License terms
├── README.md           # Technical documentation and project guide
└── portscanner.py      # Core TCP port scanning logic & CLI entry point
```

---

## 🔬 Technical Overview

The utility operates at the **Transport Layer (Layer 4)** of the OSI model. It uses standard TCP stream sockets (`socket.SOCK_STREAM`) to attempt a TCP connection against the target host.

### TCP Connection Flow

```text
  [ Client ]                              [ Target Host ]
      |                                         |
      | ------------- SYN (Port X) -----------> |
      | <---------- SYN-ACK (Port Open) ------- |  ===> connect_ex() = 0
      |                                         |
      | <---------- RST/ACK (Port Closed) ----- |  ===> connection refused
      |                                         |
```

### Connection Mechanics: `connect()` vs `connect_ex()`

Instead of using `socket.connect()`—which raises a `socket.error` exception on failure—the scanner leverages `socket.connect_ex()`.

`connect_ex()` returns `0` upon successful TCP connection establishment:

```text
0 = Port OPEN
```

It returns an explicit error code when a connection cannot be established, such as:

```text
111   = ECONNREFUSED on Linux
10061 = WSAECONNREFUSED on Windows
```

Timeouts and other socket errors can indicate that a port is filtered, unreachable, or otherwise unavailable.

---

## 🚀 Usage Guide

### Prerequisites

* Python 3.6+ installed on your system
* Network connectivity to the target host

### Installation & Execution

Clone the repository:

```bash
git clone https://github.com/void-syntax/port-scanner.git
cd port-scanner
```

Run the script:

```bash
python3 scanner.py
```

### Sample Output

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

## 📌 Roadmap & Future Enhancements

* [ ] **Multi-threading:** Integrate `concurrent.futures.ThreadPoolExecutor` for asynchronous parallel port processing.
* [ ] **Custom Port Arguments:** Add CLI flags via `argparse` to allow scanning specific ports or ranges (e.g., `-p 1-1024`).
* [ ] **Banner Grabbing:** Read initial socket payloads to identify running service versions.
* [ ] **Structured Export:** Add support for saving scan results directly to JSON or CSV files (`--output scan.json`).

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the Project
2. Create your Feature Branch:

```bash
git checkout -b feature/AmazingFeature
```

3. Commit your Changes:

```bash
git commit -m "Add some AmazingFeature"
```

4. Push to the Branch:

```bash
git push origin feature/AmazingFeature
```

5. Open a Pull Request

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## ⚠️ Legal & Security Disclaimer

> **Warning:** This tool is designed exclusively for educational purposes, defensive security auditing, and authorized administrative tasks.
>
> Scanning networks or hosts without prior explicit authorization from the target owner may be illegal and may violate applicable cybercrime laws, organizational policies, or ISP terms of service.
>
> The author assumes no liability for misuse or damage caused by this software. Only scan systems and networks that you own or have explicit permission to test.
