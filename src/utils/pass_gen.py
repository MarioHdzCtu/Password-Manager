import secrets
import string

chars = string.punctuation + string.ascii_letters + string.digits


def generate_password(lenght: int):
    password = ''.join(secrets.choice(chars) for _ in range(lenght))
    return password
