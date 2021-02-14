# File: encrypt.py
from load_file import load_file, save_file

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(sheet):
    """Function to encrypt a message."""
    file_content = load_file('plaintext.txt')


    for line in file_content:
        ciphertext = ''
        for position, character in enumerate(line):
            if character not in ALPHABET:
                ciphertext += character
            else:
                encrypted = (ALPHABET.index(character) + int(sheet[position])) % 26
                ciphertext += ALPHABET[encrypted]
        #print(f"{ciphertext}")
        save_file('ciphertext.txt', ciphertext+'\n')


def decrypt(ciphertext, sheet):
    plaintext = ''
    for position, character in enumerate(ciphertext):
        if character not in ALPHABET:
            plaintext += character
        else:
            decrypted = (ALPHABET.index(character) - int(sheet[position])) % 26
            plaintext += ALPHABET[decrypted]
    print(plaintext)
