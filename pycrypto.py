# made with <3 by Dan Goodman, signed 10/2/2017

# The imports
import hashlib
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from time import sleep
import Crypto.Util.Counter
import random
import os
from time import sleep
from sys import platform
import random
import sys

# Menu time

# iv = random.randint(0, 99)

# encryption function
# def encryptfile(in_filename, out_filename = None)
def encryptfile():
    # if not out_filename:
    in_filename = input("So where is that file you want to encrypt?\n> ")
    out_filename = input("And what do you want the output name to be? (No extension)\n(Leave blank to just add .pcr extension)\n> ")
    
    # try to avoid breaking the extension
    if out_filename == '':
        out_filename = in_filename + '.pcr'
    # in case they added the extension
    elif '.' in out_filename:
        out_filename = out_filename + '.pcr'
    else:
        # out_filename = out_filename + infilename[-4:] + '.pcr'
        inhead, insep, inext = in_filename.partition('.')
        out_filename = out_filename + insep + inext + '.pcr'
    
    # key stuff
    print("So what is the key (password) going to be for this?")
    sleep(0.2)
    key = input('> ')
    hashkey = SHA256.new()
    hashkey.update(key.encode())
    # print("The hash digest is", hashkey.digest())
    hashed_key = hashkey.digest()
    
    # get that iv
    print("So what is the iv (that integer)?")
    sleep(0.2)
    iv = int(input("> "))
    
    # encryption time
    ctr = Crypto.Util.Counter.new(128, initial_value = iv)
    encryptor = AES.new(hashed_key, AES.MODE_CTR, counter = ctr)
    infile = open(in_filename, 'rb')
    outfile = open(out_filename, 'wb')
    data  = infile.read()
    outfile.write(encryptor.encrypt(data))
    infile.close()
    outfile.close()
    
# #encryptfile('testin.txt')
# encryptfile('testin.txt', iv)
# decryption function

# def decryptfile(in_filename, iv, out_filename = None)
# def decryptfile(in_filename, out_filename  = None):
def decryptfile():
    in_filename = input("So where is that file you want to decrypt?\n> ")
    out_filename = input("And what do you want the output name to be?\n(Leave blank to just remove .pcr extension and prefix with: 'decrypted')\n> ")
    
    if out_filename == '':
        out_filename = 'decrypted' + in_filename[:-4]
        
    # key stuff
    print('Hey what was that key again?')
    sleep(0.2)
    newkey = input('> ')
    newhashkey = SHA256.new()
    newhashkey.update(newkey.encode())
    # print("The hash digest is", newhashkey.digest())
    newhashed_key = newhashkey.digest()
    
    # get that iv    # get that iv
    print("So what is the iv (that integer)?")
    sleep(0.2)
    iv = int(input("> "))
    
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
# #decryptfile('testin.txt.pcr', 'testout.txt')

def header():
    print(bcolors.purple + """
    \n
██████╗ ██╗   ██╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗ ██████╗ ██████╗ 
██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██████╔╝ ╚████╔╝ ██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║   ██║██████╔╝
██╔═══╝   ╚██╔╝  ██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║   ██║██╔══██╗
██║        ██║   ╚██████╗██║  ██║   ██║   ██║        ██║   ╚██████╔╝██║  ██║
╚═╝        ╚═╝    ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝    ╚═════╝ ╚═╝  ╚═╝
    """ + bcolors.yellow + " Made with" + bcolors.red + " ❤ " + bcolors.yellow + "By Dan Goodman\n " + bcolors.endcolor)

# fairly self descriptive, but it clears the screen depending on os type
def clearscreen():
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        # Linux or MacOS
        os.system('clear')
    elif platform == "win32":
        # Windows
        os.system('cls')

# get them colors going
class bcolors:
    purple = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    endcolor = '\033[0m'
    whitebold = '\033[1m'
    underline = '\033[4m'
    cyan = '\u001b[36m'
    cyanbold = '\u001b[36;1m'
    redbold = '\u001b[31;1m'
    yellowbold = '\u001b[33;1m'
    greenbold = '\u001b[32;1m'
    bluebold = '\u001b[34;1m'
    magentabold = '\u001b[35;1m'
    purplebold = '\u001b[35;1m'
    whitebolder = '\u001b[37;1m'
    reset = '\u001b[0m'
    

# the menu items
def menuitems():
    print(bcolors.whitebolder + "Menu Options:" + bcolors.reset)
    sleep(0.1)
    print(bcolors.cyanbold + "E: Encrypt a file" + bcolors.endcolor)
    sleep(0.1)
    print(bcolors.cyanbold + "D: Decrypt a file" + bcolors.endcolor)
    sleep(0.1)
    print(bcolors.red + "Q: Quit the program" + bcolors.endcolor)
    
def typeoutmenuitems():
    line1 = "\n" + bcolors.whitebolder + "Menu Options:" + bcolors.reset
    for i in line1:
        print(i, end='')
        sys.stdout.flush()
        sleep(0.05)
    
    sleep(0.05)
    line2 = "\n" + bcolors.cyanbold + "E: Encrypt a file" + bcolors.endcolor
    for i in line2:
        print(i, end='')
        sys.stdout.flush()
        sleep(0.05)
        
    sleep(0.05)
    line3 = "\n" + bcolors.cyanbold + "D: Decrypt a file" + bcolors.endcolor
    for i in line3:
        print(i, end='')
        sys.stdout.flush()
        sleep(0.05)
        
    sleep(0.05)
    line4 = "\n" + bcolors.red + "Q: Quit the program" + bcolors.endcolor + "\n"
    for i in line4:
        print(i, end='')
        sys.stdout.flush()
        sleep(0.05)

# menu function
def menu():
    try:
        choice = ''
        while choice not in ['e', 'E', 'd', 'D', '1', '2', 'q', 'Q']:
            clearscreen()
            header()
            sleep(0.2)
            menuitems()
            sleep(0.4)
            choice = input('> ')
            if choice == 'e' or choice == 'E':
                encryptfile()
            elif choice == 'd' or 'D':
                decryptfile()
            elif choice == 'q' or choice == 'Q':
                exit(0)
    except KeyboardInterrupt:
        print("You want to leave so early?\nI thought we were just getting started!")


# The main function
def main():
    menu()
    
    

main()