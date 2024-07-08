from ..models import Account, Response
from ..database import db
from fastapi import HTTPException


class AccountService:

    def __init__(self) -> None:
        pass

    def save_account(self, account: Account):
        query = """INSERT INTO
        password_mng.passwords(platform, username, password, note, iv)
        VALUES (?,?,?,?,?)"""
        vals = account.get_values()
        with db as conn:
            rows = conn.insert(query=query, data=vals)
        if rows != 1:
            raise ValueError

    def retrive_account(self, account_id: int = None):
        id_query = "AND id = ?" if account_id is not None else ""
        query = "SELECT * FROM password_mng.passwords WHERE 1=1 " + id_query
        vals = (account_id,) if account_id is not None else ()
        with db as conn:
            res: list[dict] = conn.select(query=query, vals=vals)
        if not res:
            raise HTTPException(status_code=404, detail= f'No account was found with id {account_id}')
        return res
