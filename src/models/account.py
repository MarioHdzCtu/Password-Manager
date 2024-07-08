from typing import Any
from pydantic import BaseModel


class Account(BaseModel):
    user_id: int
    platform: str
    username: str
    password: str | bytes
    note: str | None = None
    iv: bytes | str | None = None

    def get_values(self) -> tuple:
        return self.platform, self.username, self.password, self.note, self.iv
