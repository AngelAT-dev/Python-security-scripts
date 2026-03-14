network_traffic.txt
192.168.1.10 22
192.168.1.10 23
192.168.1.10 80
192.168.1.10 443
192.168.1.10 21
192.168.1.10 25
192.168.1.20 80
192.168.1.20 443

from collections import defaultdict

traffic_file = "network_traffic.txt"

port_activity = defaultdict(set)

with open(traffic_file, "r") as file:
    lines = file.readlines()

for line in lines:
    parts = line.strip().split()

    if len(parts) == 2:
        ip = parts[0]
        port = parts[1]

        port_activity[ip].add(port)

print("\nNetwork Attack Detection\n")

for ip, ports in port_activity.items():
    if len(ports) > 5:
        print(f"Possible port scan detected from {ip}")
