import socket
from datetime import datetime

target = input("Enter target IP or hostname: ")

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Hostname could not be resolved.")
    exit()

print("-" * 50)
print(f"Scanning target: {target_ip}")
print(f"Scan started at: {datetime.now()}")
print("-" * 50)

for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    result = s.connect_ex((target_ip, port))

    if result == 0:
        print(f"Port {port} is OPEN")

    s.close()

print("-" * 50)
print("Scan completed.")
