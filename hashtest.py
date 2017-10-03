from Crypto.Hash import SHA256

message = 'test message'
hashmessage = SHA256.new()
hashmessage.update(message.encode())
print("The hash digest is", hashmessage.digest())
hashed_message = hashmessage.digest()

dehashmessage = SHA256.new()
dehashmessage.update(hashed_message)