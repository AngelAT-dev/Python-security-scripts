from collections import Counter

log_file = "access_log.txt"

with open(log_file, "r") as file:
    lines = file.readlines()

ips = []

for line in lines:
    parts = line.split()
    if len(parts) > 0:
        ips.append(parts[0])

counter = Counter(ips)

print("Suspicious IP activity:\n")

for ip, count in counter.items():
    if count > 5:
        print(f"IP {ip} has {count} requests (possible attack)")
