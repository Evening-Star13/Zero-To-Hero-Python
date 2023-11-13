"""Password Generator"""
import string
import secrets
alphabet = string.ascii_letters + string.digits
while True:
    password = ''.join(secrets.choice(alphabet) for i in range(15))
    if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 3):
        break
alphabet1 = string.ascii_letters + string.digits
password1 = ''.join(secrets.choice(alphabet) for i in range(8))
