import socket

target = input("Enter a domain or IP: ")

try:
    ip = socket.gethostbyname(target)
    print("IP address:", ip)

    hostname = socket.gethostbyaddr(ip)
    print("Hostname:", hostname[0])

except socket.error:
    print("Could not retrieve information.")
