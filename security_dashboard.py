from collections import Counter

log_file = "security_log.txt"

with open(log_file, "r") as file:
    logs = file.readlines()

events = []

for line in logs:
    parts = line.strip().split(" - ")
    if len(parts) > 1:
        events.append(parts[1])

counter = Counter(events)

print("\nSecurity Event Dashboard\n")

for event, count in counter.items():
    print(f"{event}: {count}")
