from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from pathlib import Path
import os

key_path = Path.home()/'Documents'


def generate_key(password):
    if check_if_key_exist():
        return 'The key already exists'
    key = PBKDF2(password, get_random_bytes(32), dkLen=32)
    with open(key_path/'key.bin', 'wb') as f:
        f.write(key)
    return f'The key was saved on {key_path}/key.bin'


def check_if_key_exist():
    return os.path.exists(key_path/'key.bin')

