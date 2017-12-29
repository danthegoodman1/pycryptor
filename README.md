# pythonAES/pyCryptor


## (WIP) My own Python encryption program (See testing branch for most updated version)


## Installation:

- git clone the repo (obviously)
- cd into the repo
- run in terminal:
`sudo -H pip3 install pycrypto`
- when complete, you are ready to run:
`python3 pycryptor.py`!!!



## pycryptor.py (WIP):
Currently can:

- Take files and encrypt them
- Take files and decrypt them
- Uses custom .pcr file type (pyCryptor is the idea...)
- Hashes the key using SHA256(may update to SHA512)
- Support for any extension length
- Robust naming algorithm when encrypting files to not break original file extension

To-Do:

- add option to go back to main menu after encrypt or decrypt functions finish
- Color the print statements inside of the encrypt and decrypt functions
- Maybe make key handling a function?



## Completed:

- Convert into helper functions
- Make use for string or file
- Implement support for files
- Combine CBC and CTR into single program and give user option
- Finish making the out\_filename optional
- Make iv's not a random int from 0-98 (make an additional user input alongside the key), make it random bytes (using urandom) converted to an integer
- Finish install instructions
- Make more user friendly (a nice cli menu to hold the user's hand)
- integrate random iv generation (removing user input)