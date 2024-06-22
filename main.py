from src.services import KeyService, get_key_service, CipherService, AccountService, get_cipher_service
from src.models import Account
from fastapi import FastAPI, Depends
import uvicorn


app = FastAPI()


def get_key_service_instance():
    return get_key_service()


def get_cipher_service_instance(key_service: KeyService = Depends(get_key_service_instance)):
    key = key_service.get_key()
    return get_cipher_service(key=key)


@app.get('/generate_key')
def generate_key(
        password: str,
        key_service: KeyService = Depends(get_key_service)):

    # key = key_service.generate_key(password)
    return {'msg': "Key generated correctly"}


@app.post('/new-account')
def new_account(account: Account,
                key_service: KeyService = Depends(get_key_service_instance),
                cipher_service: CipherService = Depends(
                    get_cipher_service_instance)):

    account.password, account.iv = cipher_service.encrypt_str(account.password.encode('utf-8'))

    account_service = AccountService()

    account_service.save_account(account=account)

    return account.username


@app.get('/account')
def get_account(account_id: int = None,
                cipher_service: CipherService = Depends(get_cipher_service_instance)):
    account_service = AccountService()
    account: dict = account_service.retrive_account()
    account['password'] = cipher_service.decrypt_str(account['password'], iv=account['iv'])
    account['iv'] = None
    account = Account(**account)

    return account


if __name__ == '__main__':

    uvicorn.run(app, host="0.0.0.0", port=8000)
