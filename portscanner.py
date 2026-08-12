import socket

target = input("Enter IP address or domain: ")

ports_to_scan = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 8080]

try:
    target_ip = socket.gethostbyname(target)
    print(f"\n[+] Scanning: {target} ({target_ip})")
    print("-" * 35)

    for port in ports_to_scan:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port:<5} : OPEN")

        s.close()

except socket.gaierror:
    print("\n[-] Error: Could not resolve host IP address.")
except KeyboardInterrupt:
    print("\n[!] Scanning interrupted by user.")
except Exception as e:
    print(f"\n[-] An error occurred: {e}")

print("-" * 35)
print("Scanning complete.")
