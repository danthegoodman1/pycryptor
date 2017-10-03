import hashlib
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from time import sleep
import Crypto.Util.Counter
import random
import os


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

# ctr = Crypto.Util.Counter.new(NUM_COUNTER_BITS)

# use os.urandom(16) to get 16 random bytes and convert to int
iv = random.randint(0, 99)
# ivbytes = os.urandom(16)
print(iv)
ctr = Crypto.Util.Counter.new(128, initial_value = iv)

# do some encryption now

obj = AES.new(hashed_key, AES.MODE_CTR, counter = ctr)

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
newctr = Crypto.Util.Counter.new(128, initial_value = iv)

obj2 = AES.new(newhashed_key, AES.MODE_CTR, counter = newctr)

decrypted = obj2.decrypt(ciphertext)
print("The decrypted message is:", decrypted.decode(encoding='UTF-8'))

