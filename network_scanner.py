import socket

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

print("Your IP address:", local_ip)

base_ip = ".".join(local_ip.split(".")[:-1]) + "."

print("Scanning local network...\n")

for i in range(1, 255):
    ip = base_ip + str(i)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex((ip, 80))

    if result == 0:
        print(f"Device found at {ip}")

    sock.close()
