from dataclasses import dataclass
from pathlib import Path
import os


@dataclass
class Key:
    """
    Key class representing the result of the Crypto.Protocol.KDF.PBKDF2 operation.
    Manages the read/write of the encryption key
    """
    content: bytes

    key_path: str = Path.home()/'Documents'
    file_name: str = 'key.bin'

    def save_key(self):
        with open(self.key_path/self.file_name, 'wb') as f:
            f.write(self.content)

    def check_if_key_exist(self):
        return os.path.exists(self.key_path/self.file_name)