from dataclasses import dataclass
from pathlib import Path
import os
# from ..exceptions.key_exists import KeyAlreadyExists


@dataclass
class Key:
    """
    Key class representing the result of the Crypto.Protocol.KDF.PBKDF2 operation.
    Manages the read/write of the encryption key
    """
    content: bytes
    key_path: str
    file_name: str

    def save_key(self):
        if self.key_exist:
            return False, "", "The key already exists. Re-writing the key will make any encrypted content unsusable. No new key was registered", 409
        with open(self.key_path/self.file_name, 'wb') as f:
            f.write(self.content)
        return True, str(self.key_path/self.file_name), "The key was created successfully", 200

    @property
    def key_exist(self):
        return os.path.exists(self.key_path/self.file_name)
