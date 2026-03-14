from collections import defaultdict

log_file = "system_logs.txt"

failed_logins = defaultdict(int)

with open(log_file, "r") as file:
    logs = file.readlines()

for line in logs:
    parts = line.strip().split()

    if len(parts) >= 2:
        ip = parts[0]
        event = parts[1]

        if event == "LOGIN_FAILED":
            failed_logins[ip] += 1

print("\nSecurity Alerts\n")

for ip, count in failed_logins.items():
    if count >= 5:
        print(f"ALERT: Possible brute force attack from {ip} ({count} failed logins)")
