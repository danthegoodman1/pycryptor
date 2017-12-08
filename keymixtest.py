# made with <3 by Dan Goodman, signed 10/2/2017

# Thanks to Andy Novocin for help with iv handling

# The imports
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from time import sleep
import Crypto.Util.Counter
import random
import os
from sys import platform
import sys
import binascii
import sqlite3
from Crypto.PublicKey import RSA
import os.path

# Andy's part
num_bytes = 32
ivbytes = os.urandom(num_bytes)

def bytes2int(rawbytes):
  return int(binascii.hexlify(rawbytes),16)

def int2bytes(bigint, n_bytes):
  return binascii.unhexlify(format(bigint, 'x').zfill(n_bytes*2))

intiv = bytes2int(ivbytes)
rawbytesiv = int2bytes(intiv, num_bytes)

# check keys, and generate if don't exist, generate in PEM format because 1) pycrypto won't generate openssh keys 2) We aren't using these for ssh
def check_keygen():
    if os.path.isfile('private.pem') == True and os.path.isfile('public.pem') == True:
        print("keys already exist!")
    else:
        keypair = RSA.generate(4096)
        with open("private.pem", 'wb') as content_file:
            # chmod("private.pem", 0600)
            content_file.write(keypair.exportKey('PEM'))
        pubkey = keypair.publickey()
        with open("public.pem", 'wb') as content_file:
            content_file.write(pubkey.publickey().exportKey('PEM'))
    print("RSA keys have been generated")
    sleep(0.1)
    
def mix_keys(contactkey):
    f = open('private.pem')
    myprivkey = RSA.importKey(f.read())
    theirpubkey = RSA.importKey(contactkey)
    privkeyint = bytes2int(myprivkey)
    theirpubkeyint = bytes2int(theirpubkey)
    mixedkeyint = # the function to mix the keys
    realmixedkey = int2bytes(mixedkeyint)
    return realmixedkey

# get password function
def get_password():
    clearscreen()
    header()
    print("So what is the key (password) going to be for this?")
    sleep(0.2)
    key = input('> ')
    hashkey = SHA256.new()
    hashkey.update(key.encode())
    hashed_key = hashkey.digest()
    return hashed_key

# get user key function %%% This is going to change to sqlite when I get that working how I want
def get_pubkey(name):
    clearscreen()
    header()
    # get and display contacts, maybe I can use a dictionary here
    c.execute("SELECT name FROM funtimes WHERE name = {0}".format(name))
    row = c.fetchone()
    print("You have selected {0}, to be the recipient for the encrypted file (only they can open it!!!) continue? (Y/N)".format(row[0]))
    sleep(0.1)
    try:
        choice = ''
        while choice not in ['Y', 'y', 'N', 'n']:
            choice = input("> ")
            if choice == 'Y' or choice == 'y':
                pubkey = row[1]
            elif choice == 'n' or choice == 'N':
                main()
            else:
                print("Well I would love if you could give me something I knew what to do with...")
                sleep(0.5)
    except KeyboardInterrupt:
        print("You want to leave so early?\nI thought we were just getting started!")
        closetable()
    return pubkey

# gets pubkey or password
def get_key():
    try:
        selection = ''
        selectionlist = ['p', 'P', 'q', 'Q', 'k', 'K']
        while selection not in selectionlist:
            clearscreen()
            header()
            print("So, how do you want to protect the file?") 
            sleep(0.2)
            print("P: Password\nK: Keys\nQ: Quit")
            selection = input("> ")
            if selection == 'p' or selection == 'P':
                key = get_password()
            elif selection == 'k' or selection == 'K':
                print("So who are you looking for?")
                sleep(0.1)
                name = input("> ")
                key = mix_keys(get_pubkey(findpersonfromname(name)))
            elif selection == 'q' or selection == 'Q':
                print("You want to leave so early?\nI thought we were just getting started!")
                sleep(1)
                closetable()
                exit(0)
            else:
                print("I would really appreciate input that I know what to do with...")
                sleep(1.3)
            return key
    except KeyboardInterrupt:
        print("You want to leave so early?\nI thought we were just getting started!")
        closetable()

# The sqlite section (yay)

conn = sqlite3.connect('contacts.db')
c = conn.cursor()

def closetable():
    c.close()
    conn.close()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS contacts(name KEYWORD, pubkey KEYWORD)")

def searchforcontact():
    clearscreen()
    header()
    print('So who are we looking for?')
    sleep(0.05)
    name = input("> ")
    c.execute("SELECT name FROM funtimes WHERE name LIKE '%{}%'".format(name))
    num = 0
    namelist = []
    print("These are the people I found with {0} in their name".format(name))
    for row in c.fetchall():
        num += 1
        namelist.append(row[0])
        print(num, "\b:", "'{}'".format(row[0]))
    sleep(0.1)
    print("When you are ready to go back to the main menu just hit enter")
    pointlessvar = input("")
    main()

def findpersonfromname(name):
    clearscreen()
    header()
    c.execute("SELECT name FROM funtimes WHERE name LIKE '%{}%'".format(name))
    num = 0
    namelist = []
    for row in c.fetchall():
        num += 1
        namelist.append(row[0])
        print(num, "\b:", "'{}'".format(row[0]))
    sleep(0.05)
    print("now choose someone (input the number)")
    sleep(0.1)
    choice = int(input("> "))
    chosen = namelist[(choice - 1)]
    sleep(0.1)
    print("The user:", "'{0}'".format(chosen), "has been selected")
    return chosen
    
def addcontact():
    clearscreen()
    header()
    print("Alright, so what is the name of this person that you want to add to your contacts?")
    sleep(0.05)
    name = input("> ")
    sleep(0.1)
    # maybe make them point to the file and then import it?
    print("And what is their pubkey? (Please make sure you copy it correctly)")
    sleep(0.05)
    pubkey = input("> ")
    c.execute("INSERT INTO funtimes VALUES('{0}', '{1}')".format(name, pubkey,))
    sleep(0.2)
    print("Done!... Added {0} with their public key".format(name))
    main()
    
def removecontact():
    clearscreen()
    header()
    print("Alright, so what is the name of this person that you want to remove from your contacts?")
    sleep(0.05)
    name = input("> ")
    sleep(0.1)
    pubkey = input("> ")
    c.execute("SELECT name FROM funtimes WHERE name LIKE '%{}%'".format(name))
    num = 0
    namelist = []
    for row in c.fetchall():
        num += 1
        namelist.append(row[0])
        print(num, "\b:", "'{}'".format(row[0]))
    sleep(0.05)
    print("now choose someone (input the number)")
    sleep(0.1)
    choice = int(input("> "))
    chosen = namelist[(choice - 1)]
    sleep(0.05)
    print("Are you sure you want to remove {0} ?\n They will be gone forever... DUN DUNNNNNN!!!!!    (Y/N)".format(chosen))
    sleep(0.1)
    check = 0
    while check not in ['y', 'Y', 'n', 'N']:
        check = input("> ")
        if check == 'Y' or check == 'y':
            sleep(0.1)
            # REMOVE THE CONTACT
            print("The user:", "'{0}'".format(chosen), "has been removed")
            sleep(0.2)
            print("Done!... Added {0} with their public key".format(name))
        elif check == 'N' or check == 'n':
            print("Aborted")
        else:
            print("Please select Y or N")
    main()

# 
# 
# 
# 
# 
# 
# 
# 
# 


# encryption function
def encryptfile(in_filename = None, out_filename = None):
    # These if statements allow for optional argument passing
    if in_filename == None:
        # if not out_filename:
        in_filename = input("So where is that file you want to encrypt?\n> ")
    if out_filename == None:
        # can remove the (No extension) part
        out_filename = input("And what do you want the output name to be?\n(Leave blank to just add .pcr extension)\n> ")
    
    # try to avoid breaking the extension
    if out_filename == '':
        out_filename = in_filename + '.pcr'
    # in case they added the extension, and hoping that the last character of the name is not a '.'
    elif out_filename[-3] == '.' or out_filename[-4] == '.':
        out_filename = out_filename + '.pcr'
    else:
        # out_filename = out_filename + infilename[-4:] + '.pcr'
        # this method gives easy of file type handling for the future (hoping that the last character before the extension isn't a . lol)
        if in_filename[-3] == '.':
            out_filename = out_filename + in_filename[-3:] + '.pcr'
        elif in_filename[-4] == '.':
            out_filename = out_filename + in_filename[-4:] + '.pcr'
    
    # key handling
    key = get_key()
    
    num_bytes = 32
    ivbytes = os.urandom(num_bytes)

    intiv = bytes2int(ivbytes)
    rawbytesiv = int2bytes(intiv, num_bytes)
    
    # encryption time
    ctr = Crypto.Util.Counter.new(128, initial_value = intiv)
    encryptor = AES.new(key, AES.MODE_CTR, counter = ctr)
    infile = open(in_filename, 'rb')
    outfile = open(out_filename, 'wb')
    data  = infile.read()
    # outfile_content = "{0}{1}".format(rawbytesiv, encryptor.encrypt(data))
    outfile.write(rawbytesiv + encryptor.encrypt(data))
    infile.close()
    outfile.close()

def decryptfile(in_filename = None, out_filename = None):
    # These if statements allow for optional argument passing
    if in_filename == None:
        in_filename = input("So where is that file you want to decrypt?\n> ")
    if out_filename == None:
        out_filename = input("And what do you want the output name to be?\n(Leave blank to just remove .pcr extension and prefix with: 'decrypted')\n> ")
    
    if out_filename == '':
        out_filename = 'decrypted' + in_filename[:-4]
    else: out_filename = out_filename + in_filename[:-4]

    # key handling
    key = get_key()
    
    # get the iv (first 32 bytes of data in the file)
    infileraw = open(in_filename, 'rb')
    encrypted_file = infileraw.read()
    ivbytes = encrypted_file[:32]
    numbytes = 32
    intiv = bytes2int(ivbytes)
    data = encrypted_file[32:]
    
    # decryption time
    ctr = Crypto.Util.Counter.new(128, initial_value = intiv)
    encryptor = AES.new(key, AES.MODE_CTR, counter = ctr)
    outfile = open(out_filename, 'wb')
    decryptiondata = encryptor.decrypt(data)
    print(decryptiondata)
    outfile.write(decryptiondata)
    infileraw.close()
    outfile.close()

# Fancy header
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
    print(bcolors.blue + "Version: 1.1\n" + bcolors.endcolor)

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
    print(bcolors.cyanbold + "A: Add contact" + bcolors.endcolor)
    sleep(0.1)
    print(bcolors.cyanbold + "R: Remove contact" + bcolors.endcolor)
    sleep(0.1)
    print(bcolors.cyanbold + "S: Search for contacts" + bcolors.endcolor)
    sleep(0.1)
    print(bcolors.red + "Q: Quit the program" + bcolors.endcolor)

# menu items with a fancy typing look (can add randomness to make it look more like typewriter but it takes too long this way anyway)
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

# menu function... it's the menu
def menu():
    try:
        choice = ''
        while choice not in ['e', 'E', 'd', 'D', '1', '2', 'q', 'Q', 'a', 'A', 'r', 'R', 's', 'S']:
            clearscreen()
            header()
            sleep(0.2)
            menuitems()
            sleep(0.2)
            choice = input('> ')
            if choice == 'e' or choice == 'E':
                encryptfile()
            elif choice == 'd' or 'D':
                decryptfile()
            elif choice == 'A' or choice == 'a':
                addcontact()
            elif choice == 'R' or choice == 'r':
                removecontact()
            elif choice == 's' or choice == 'S':
                searchforcontact()
            elif choice == 'q' or choice == 'Q':
                print("You want to leave so early?\nI thought we were just getting started!")
                sleep(1)
                closetable()
                exit(0)
            else:
                print("I would really appreciate input that I know what to do with...")
                sleep(1.3)
    except KeyboardInterrupt:
        print("You want to leave so early?\nI thought we were just getting started!")
        closetable()


# The main function (That is currently calling one function...)
def main():
    menu()
    
check_keygen()
create_table()
main()
