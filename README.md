# pythonAES/pyCryptor


## (WIP) My own Python encryption program


## Installation:

- git clone the repo (obviously)
- cd into the repo
- run in terminal:
`sudo python3 install.py`
- when complete, you are ready to run:
`python3 pycryptor.py`!!!



## pycryptor.py (WIP):
Currently can:

- Take files and encrypt them
- Take files and decrypt them
- Uses custom .pcr file type (pyCryptor is the idea...)
- Hashes the key using SHA256(may update to SHA512)

To-Do:

- Make more user friendly (a nice cli menu to hold the user's hand)
- converting a string into an int for iv
- add option to go back to main menu after encrypt or decrypt functions finish
- Color the print statements inside of the encrypt and decrypt functions
 
## Project To-Do:
- make install script

## Completed:

- Convert into helper functions
- Make use for string or file
- Implement support for files
- Combine CBC and CTR into single program and give user option
- Finish making the out\_filename optional
- Make iv's not a random int from 0-98 (make an additional user input alongside the key), make it random bytes (using urandom) converted to an integer