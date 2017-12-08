from Crypto.PublicKey import RSA
import os.path


def checkkeygen():
    if os.path.isfile('private.pem') == True and os.path.isfile('public.pem') == True:
        print("keys already exist!")
    else:
        keypair = RSA.generate(4096)
        with open("private.pem", 'wb') as content_file:
            # chmod("private.key", 0600)
            content_file.write(keypair.exportKey('PEM'))
        pubkey = keypair.publickey()
        with open("public.pem", 'wb') as content_file:
            content_file.write(pubkey.publickey().exportKey('PEM'))
    print("RSA keys have been generated")
            
checkkeygen()