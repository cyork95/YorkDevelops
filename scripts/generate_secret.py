import secrets
import string

alphabet = string.ascii_letters + string.digits + string.punctuation
secret_key = ''.join(secrets.choice(alphabet) for i in range(64))

print(secret_key)