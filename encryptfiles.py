# made with <3 by Dan Goodman, signed 10/2/2017
# this was quite helpful: https://eli.thegreenplace.net/2010/06/25/aes-encryption-of-files-in-python-with-pycrypto , but I also used a lot of my own code from 'do some encryption CTR.py'

import hashlib
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from time import sleep
import Crypto.Util.Counter
import random
import os

iv = random.randint(0, 99)

# encryption function

def encryptfile(in_filename, iv, out_filename = None):
    if not out_filename:
        out_filename = in_filename + '.pcr'
    
    # key stuff
    print("So what is the key (password) going to be for this?")
    sleep(0.2)
    key = input('> ')
    hashkey = SHA256.new()
    hashkey.update(key.encode())
    print("The hash digest is", hashkey.digest())
    hashed_key = hashkey.digest()
    
    # encryption time
    ctr = Crypto.Util.Counter.new(128, initial_value = iv)
    encryptor = AES.new(hashed_key, AES.MODE_CTR, counter = ctr)
    infile = open(in_filename, 'rb')
    outfile = open(out_filename, 'wb')
    data  = infile.read()
    outfile.write(encryptor.encrypt(data))
    infile.close()
    outfile.close()
    
encryptfile('testin.txt', iv)
# decryption function

# def decryptfile(in_filename, iv, out_filename = None)
def decryptfile(in_filename, iv, out_filename):
    if not out_filename:
        out_filename = 'decrypted' + in_filename[:-4]
        
    # key stuff
    print('Hey what was that key again?')
    sleep(0.2)
    newkey = input('> ')
    newhashkey = SHA256.new()
    newhashkey.update(newkey.encode())
    print("The hash digest is", newhashkey.digest())
    newhashed_key = newhashkey.digest()
    
    # decryption time
    ctr = Crypto.Util.Counter.new(128, initial_value = iv)
    encryptor = AES.new(newhashed_key, AES.MODE_CTR, counter = ctr)
    infile = open(in_filename, 'rb')
    outfile = open(out_filename, 'wb')
    data  = infile.read()
    outfile.write(encryptor.decrypt(data))
    infile.close()
    outfile.close()

# decryptfile('testin.txt.pcr', iv)
decryptfile('testin.txt.pcr', iv, 'testout.txt')