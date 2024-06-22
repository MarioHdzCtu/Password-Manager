from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class Cipher:

    def __init__(self, key) -> None:
        self.key = key

    def __generate_aes__(self):
        self.aes = AES.new(self.key, AES.MODE_CBC)

    def encrypt_str(self, msg: str) -> bytes:
        self.__generate_aes__()
        return self.aes.encrypt(pad(msg, AES.block_size))

    @property
    def iv(self):
        return self.aes.iv

    def decrypt_str(self, encrypted_msg: bytes, iv: bytes | str) -> str:
        cipher = AES.new(self.key, AES.MODE_CBC, iv=iv)
        return unpad(
            cipher.decrypt(encrypted_msg),
            AES.block_size).decode('utf-8')
