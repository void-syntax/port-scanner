import socket

target = input("Введите IP-адрес или домен: ")

ports_to_scan = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 8080]

try:
    target_ip = socket.gethostbyname(target)
    print(f"\n[+] Сканирование: {target} ({target_ip})")
    print("-" * 35)

    for port in ports_to_scan:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"Порт {port:<5} : ОТКРЫТ")

        s.close()

except socket.gaierror:
    print("\n[-] Ошибка: Не удалось получить IP-адрес хоста.")
except KeyboardInterrupt:
    print("\n[!] Сканирование прервано пользователем.")
except Exception as e:
    print(f"\n[-] Произошла ошибка: {e}")

print("-" * 35)
print("Сканирование завершено.")
