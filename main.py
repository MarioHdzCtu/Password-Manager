from src.utils.gen_key import generate_key
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


password = 'mypass'

key = generate_key(password)
print(key)
# message = b'Hello secret World'

# cipher = AES.new(key, AES.MODE_CBC)
# ciphered_data = cipher.encrypt(pad(message, AES.block_size))

# with open('ecrypted.bin', 'wb') as f:
#     f.write(cipher.iv)
#     f.write(ciphered_data)

# with open('ecrypted.bin', 'rb') as f:
#     iv = f.read(16)
#     encrypted_data = f.read()

# chiper = AES.new(key, AES.MODE_CBC, iv=iv)
# original = unpad(chiper.decrypt(encrypted_data), AES.block_size)

# print(original)
