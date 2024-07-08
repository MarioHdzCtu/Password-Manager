from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from ..models import Key, Response
from pathlib import Path
import toml
import sys


class KeyService:

    def __init__(
            self,
            ) -> bool:
        """Service for creating a new local key

        Args:
            password (str): The password for encrypting the key
            key_path (str, optional):NOT IMPLEMENTED YET
                The path where the key file will be saved.
                Defaults to 'Home/Documents'.
            key_name (str, optional):NOT IMPLEMENTED YET
                The name of the key file. Defaults to 'key.bin'.
        """

    def __generate_salt__(self):
        return get_random_bytes(32)

    def __write_toml_config__(self, key_path: str):

        toml_file = {
            sys.platform: {
                'key_path': key_path
            }
        }
        with open('config.toml', 'w') as f:
            toml.dump(toml_file, f)

    def generate_key(self, password: str, key_path: str = Path.home()/'Documents', key_name: str = 'key.bin'):
        salt = self.__generate_salt__()
        self.__k = PBKDF2(password=password, salt=salt, dkLen=32)
        self.key = Key(
            content=self.__k,
            key_path=key_path,
            file_name=key_name)
        self.key.save_key()
        k_path = str(key_path/key_name)
        self.__write_toml_config__(k_path)
        return self.__k

    def get_key(self):
        with open('config.toml', 'r') as f:
            config: dict = toml.load(f)
        if sys.platform not in config:
            raise FileNotFoundError
        key_path = config.get(sys.platform).get('key_path')
        with open(key_path, 'rb') as f:
            return f.read()


def get_key_service():
    return KeyService()
