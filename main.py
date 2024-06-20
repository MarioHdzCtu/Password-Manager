from src.services import KeyService

if __name__ == '__main__':
    user_password = input('Enter the password for generating a new key: ')

    keyservice = KeyService(password=user_password)
