from Crypto.PublicKey import RSA

def mix_keys():
    f = open('private.pem')
    myprivkey = RSA.importKey(f.read())
    f = open('2public.pem')
    theirpubkey = RSA.importKey(f.read())
    privkeyint = bytes2int(myprivkey)
    theirpubkeyint = bytes2int(theirpubkey)
    mixedkeyint = # the function to mix the keys GET ANDY'S HELP      # ALSO ASK ABOUT IMPORTING KEYS IN THE FORMAT FOR SQLITE3
    realmixedkey = int2bytes(mixedkeyint)
    return realmixedkey
    
print(mix_keys())

def mix_keys2():
    f = open('2private.pem')
    myprivkey = RSA.importKey(f.read())
    f = open('public.pem')
    theirpubkey = RSA.importKey(f.read())
    privkeyint = bytes2int(myprivkey)
    theirpubkeyint = bytes2int(theirpubkey)
    mixedkeyint = # the function to mix the keys GET ANDY'S HELP      # ALSO ASK ABOUT IMPORTING KEYS IN THE FORMAT FOR SQLITE3
    realmixedkey = int2bytes(mixedkeyint)
    return realmixedkey
    
print(mix_keys2())