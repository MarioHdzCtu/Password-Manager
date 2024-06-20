class KeyAlreadyExists(Exception):
    def __init__(self) -> None:
        super().__init__("The key already exists. Re-writing the key will make any encrypted content unsusable")