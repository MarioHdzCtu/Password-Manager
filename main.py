from src.services import KeyService, get_key_service, CipherService, AccountService, get_cipher_service
from src.models import Account
from src.utils import generate_password
from fastapi import FastAPI, Depends
import uvicorn


app = FastAPI()


def get_key_service_instance():
    return get_key_service()


def get_cipher_service_instance(key_service: KeyService = Depends(get_key_service_instance)):
    key = key_service.get_key()
    return get_cipher_service(key=key)


def get_account_service_instance():
    return AccountService()


@app.get('/generate_key', status_code=201)
def generate_key(
        password: str,
        key_service: KeyService = Depends(get_key_service)):

    key = key_service.generate_key(password)
    return {'msg': "Key generated correctly"}


@app.post('/new-account', status_code=201)
def new_account(account: Account,
                cipher_service: CipherService = Depends(get_cipher_service_instance),
                account_service: AccountService = Depends(get_account_service_instance)):

    account.password, account.iv = cipher_service.encrypt_str(account.password.encode('utf-8'))

    account_service.save_account(account=account)

    return account.platform, account.username


@app.get('/account', status_code=200, response_model=list[Account])
def get_account(account_id: int = None,
                cipher_service: CipherService = Depends(get_cipher_service_instance),
                account_service: AccountService = Depends(get_account_service_instance)):

    accounts = account_service.retrive_account(account_id=account_id)
    for account in accounts:
        account['password'] = cipher_service.decrypt_str(account['password'], iv=account['iv'])
        account['iv'] = None

    return accounts


@app.post('/generate-password', status_code=200)
def gen_password(lenght: int = 16) -> str:
    return generate_password(lenght=lenght)


if __name__ == '__main__':

    uvicorn.run(app, host="0.0.0.0", port=8000)
