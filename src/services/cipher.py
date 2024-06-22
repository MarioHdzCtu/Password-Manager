from ..models import Cipher


class CipherService:

    def __init__(self, key: bytes) -> None:
        self.key = key
        self.cipher = Cipher(self.key)

    def encrypt_str(self, string: str):
        return self.cipher.encrypt_str(string), self.get_iv()

    def decrypt_str(self, string: str, iv: bytes):
        return self.cipher.decrypt_str(string, iv)

    def get_iv(self):
        return self.cipher.iv


def get_cipher_service(key: bytes):
    return CipherService(key=key)
