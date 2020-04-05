#!/usr/local/bin/python3
import sys
import os
from base64 import b64encode, b64decode
from simplecrypt import encrypt, decrypt

APP_KEY=''
PASSWORD_HINT=''

def usage():
    print('===================')
    print('=====Py-Encrypt====')
    print('===================')
    print('Usage:')
    print('  cryptor [option] [flag]')
    print('Options:')
    print('  ------------')
    print('  [1] Encrypt:')
    print('  ------------')
    print('  Option = encrypt')
    print('  Description: Encrypts a file')
    print('  Flags: N/A')
    print('  ------------')
    print('  [2] Decrypt:')
    print('  ------------')
    print('  Option = decrypt')
    print('  Description: Decrypts a file')
    print('  Flags:')
    print('    --output')
    print('      (Will request an output file name rather than printing to terminal)')
    print('  ------------')
    print('  [3] Hint:')
    print('  ------------')
    print('  Option = hint')
    print('  Displays password hint')

def encryptTxt(password, txt):
    ciphertext = encrypt(password+APP_KEY, txt)
    return b64encode(ciphertext).decode('utf-8')

def decryptTxt(password, ciphertext):
    decoded_ciphertext = b64decode(ciphertext)
    try:
        return decrypt(password+APP_KEY, decoded_ciphertext)
    except:
        print("Ah ah ah... you didn't say the magic word.")
        sys.exit()

def decryptProcedure():
    filepath = input("Enter file name: ")
    #read file
    try:
        data_file = open(os.getcwd() + '/' + filepath,'r')
    except FileNotFoundError:
        print("File not found in working directory")
        sys.exit()
        
    file_contents = data_file.read()
    #decypt file contents
    text = decryptTxt(input("Enter a password: "), file_contents)
    if len(sys.argv) > 2 and sys.argv[2] == '--output':
        out_file = open(os.getcwd() + '/decrypted.txt', 'w')
        out_file.write(text.decode('utf-8'))
        out_file.close()
        print('File decrypted successfully. ("decrypted.txt" created)')
    else:
        print(text.decode('utf-8'))
        print('File decrypted successfully.')


def encryptProcedure():
    filepath = input("Enter file name: ")
    #read file
    try:
        data_file = open(os.getcwd() + '/' + filepath,'r')
    except FileNotFoundError:
        print("File not found in working directory")
        sys.exit()
    
    file_contents = data_file.read()
    #encrypt file contents
    ciphertext = encryptTxt(input("Enter a password: "), file_contents)
    #print cipher text to file
    out_file = open(os.getcwd() + '/encrypted.txt', 'w')
    out_file.write(ciphertext)
    out_file.close()
    print('File encrypted successfully. ("encrypted.txt" created)')


if __name__ == "__main__":
    #check for correct usage
    if len(sys.argv) < 2 or (sys.argv[1] != 'encrypt' and sys.argv[1] != 'decrypt' and sys.argv[1] != 'hint'):
        usage()
        sys.exit()
    #decrypt
    if sys.argv[1] == 'decrypt':
        print('decrypting...')
        decryptProcedure()
    #encrypt
    elif sys.argv[1] == 'encrypt':
        print('encrypting...')
        encryptProcedure()
    else:
        print(PASSWORD_HINT)
