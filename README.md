# pythonAES/pyCryptor


### (WIP) My own Python encryption program

### pycryptor.py (WIP):
Currently can:

- Take files and encrypt them
- Take files and decrypt them
- Uses custom .pcr file type (pyCryptor is the idea...)
- Hashes the key using SHA256(may update to SHA512)

To-Do:

- Make more user friendly (a nice cli menu to hold the user's hand)
- Make iv's not a random int from 0-98 (make an additional user input alongside the key), make it random bytes (using urandom) converted to an integer
- Finish making the out\_filename optional

### To-Do:

### Completed:

- Convert into helper functions
- Make use for string or file
- Implement support for files
- Combine CBC and CTR into single program and give user option

