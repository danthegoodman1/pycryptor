import hashlib
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

key = 'This is a key'
hashkey = ''

message = 'The answer is no'
hashmessage = SHA256.new()
hashmessage.update(message.encode())
print("The hash digest is", hashmessage.digest())

obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')

ciphertext = obj.encrypt(message)

print("The ciphered text is", ciphertext)

obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')

decrypted = obj2.decrypt(ciphertext)
decrypted = decrypted.decode(encoding='UTF-8')

print(decrypted)

# just testing stuff up here







# create menu

# encrypt

# ask for password

# hash password with sha256

# decrypt