import hashlib
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from time import sleep


# get that message

print("So, what message do you want to encrypt?")
sleep(0.2)

message = input('> ')

# now get the key

sleep(0.2)
print("So what is the key (password) going to be for this?")
sleep(0.2)
key = input('> ')

# hash the key

hashkey = SHA256.new()
hashkey.update(key.encode())
print("The hash digest is", hashkey.digest())
hashed_key = hashkey.digest()

# do some encryption now

obj = AES.new(hashed_key, AES.MODE_CBC, 'This is an IV456')

ciphertext = obj.encrypt(message)

print("The ciphered text is", ciphertext)

# get that key back

print('Hey what was that key again?')
sleep(0.2)
newkey = input('> ')

# get the key hash

newhashkey = SHA256.new()
newhashkey.update(newkey.encode())
print("The hash digest is", newhashkey.digest())
newhashed_key = newhashkey.digest()

# do some decryption now

obj2 = AES.new(newhashed_key, AES.MODE_CBC, 'This is an IV456')

decrypted = obj2.decrypt(ciphertext)
print("The decrypted message is:", decrypted.decode(encoding='UTF-8'))


# print(decrypted)

# just testing stuff up here







# create menu

# encrypt

# ask for password

# hash password with sha256

# decrypt