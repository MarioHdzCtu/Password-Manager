from pydantic import BaseModel


class Account(BaseModel):
    platform: str
    username: str
    password: str
    note: str | None = None
    iv: bytes | str | None = None

    def get_values(self) -> tuple:
        return self.platform, self.username, self.password, self.note, self.iv
