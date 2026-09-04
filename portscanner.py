import socket

target = input("Enter IP address or domain: ")

ports_to_scan = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-Proxy",
}

try:
    target_ip = socket.gethostbyname(target)
    print(f"\n[+] Scanning: {target} ({target_ip})")
    print("-" * 45)

    open_ports_count = 0

    for port, service in ports_to_scan.items():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        result = s.connect_ex((target_ip, port))

        if result == 0:
            print(f"[+] Port {port:<5} ({service:<10}) : OPEN")
            open_ports_count += 1
        else:
            print(f"[-] Port {port:<5} ({service:<10}) : CLOSED")

        s.close()

    print("-" * 45)
    if open_ports_count == 0:
        print("No open ports found.")
    else:
        print(f"Total open ports found: {open_ports_count}")

except socket.gaierror:
    print("\n[-] Error: Could not resolve host IP address.")
except KeyboardInterrupt:
    print("\n[!] Scanning interrupted by user.")
except Exception as e:
    print(f"\n[-] An error occurred: {e}")

print("Scanning complete.")
