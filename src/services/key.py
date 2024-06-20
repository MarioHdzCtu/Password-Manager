from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from ..models import Key


class KeyService:

    def __init__(
            self,
            password: str,
            key_path: str = None,
            key_name: str = None) -> None:
        """Service for creating a new local key

        Args:
            password (str): The password for encrypting the key
            key_path (str, optional):NOT IMPLEMENTED YET
                The path where the key file will be saved.
                Defaults to 'Home/Documents'.
            key_name (str, optional):NOT IMPLEMENTED YET
                The name of the key file. Defaults to 'key.bin'.
        """
        self.password = password
        self.__generate_salt__()
        self.__generate_key__()

    def __generate_salt__(self):
        self.salt = get_random_bytes(32)

    def __generate_key__(self):
        self.__k = PBKDF2(password=self.password, salt=self.salt, dkLen=32)
        self.key = Key(content=self.__k)
        self.key.save_key()
