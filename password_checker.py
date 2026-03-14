import re

password = input("Enter a password to check: ")

length = len(password) >= 8
uppercase = re.search(r"[A-Z]", password)
lowercase = re.search(r"[a-z]", password)
digit = re.search(r"\d", password)
symbol = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

score = sum([bool(length), bool(uppercase), bool(lowercase), bool(digit), bool(symbol)])

if score == 5:
    print("Strong password")
elif score >= 3:
    print("Moderate password")
else:
    print("Weak password")
