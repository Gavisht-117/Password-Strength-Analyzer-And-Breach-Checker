import hashlib
import requests


def check_breach(password): 
 hashed = hashlib.sha1(password.encode()).hexdigest()
 first5=hashed[:5]
 response = requests.get("https://api.pwnedpasswords.com/range/" + first5)
 suffix = hashed[5:].upper()
 for line in response.text.splitlines():
    hashpart, count = line.split(":")
    if hashpart == suffix:
        print(f"PWNED! Found {count} times in breaches")
        break
 else:
    print("Good news! Not found in any breaches")
 
