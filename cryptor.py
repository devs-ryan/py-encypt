#!/usr/bin/python3


###########
# IMPORTS #
###########
import sys
import os
import getpass
from base64 import b64encode, b64decode


########################
# INSTALL INSTRUCTIONS #
########################
# pip3 install simple-crypt
# pip3 uninstall PyCrypto && pip3 install -U PyCryptodome
# more info: https://pypi.org/project/simple-crypt/ & https://stackoverflow.com/a/62520082
from simplecrypt import encrypt, decrypt


####################
# GLOBAL VARIABLES #
####################
APP_KEY=''
PASSWORD_HINT=''
FILE_PATH=''


#########
# USAGE #
#########
def usage():
    print('===================')
    print('=====Py-Encrypt====')
    print('===================')
    print('Usage:')
    print('  cryptor.py [option] [flags]')
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
    print('      (Will output to file rather than printing to terminal)')
    print('    --ignore-path')
    print('      (Will use the current working directory instead of typical file path)')
    print('  ------------')
    print('  [3] Hint:')
    print('  ------------')
    print('  Option = hint')
    print('  Displays password hint')


###############
# ENCYPT TEXT #
###############
def encryptTxt(password, txt):
    ciphertext = encrypt(password+APP_KEY, txt)
    return b64encode(ciphertext).decode('utf-8')


###############
# DECYPT TEXT #
###############
def decryptTxt(password, ciphertext):
    decoded_ciphertext = b64decode(ciphertext)
    try:
        return decrypt(password+APP_KEY, decoded_ciphertext)
    except:
        print("Ah ah ah... you didn't say the magic word.")
        sys.exit()


###########
# DECRYPT #
###########
def decryptProcedure():
    filename = input("Enter file name: ")
    ignorepath = '--ignore-path' in sys.argv or '-i' in sys.argv
    filepath = FILE_PATH if (not ignorepath and FILE_PATH and FILE_PATH != '') else os.getcwd() 
    
    #read file
    try:
        data_file = open(filepath + '/' + filename, 'r')
    except FileNotFoundError:
        print("File not found in " + filepath)
        sys.exit()
        
    file_contents = data_file.read()
    
    #decypt file contents
    text = decryptTxt(getpass.getpass("Enter a password: "), file_contents)
    if '--output' in sys.argv or '-o' in sys.argv:
        out_file = open(os.getcwd() + '/decrypted.txt', 'w')
        out_file.write(text.decode('utf-8'))
        out_file.close()
        print('File decrypted successfully. ("decrypted.txt" created in current working directory)')
    else:
        print(text.decode('utf-8'))
        print('File decrypted successfully.')


###########
# ENCRYPT #
###########
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
    ciphertext = encryptTxt(getpass.getpass("Enter a password: "), file_contents)
    #print cipher text to file
    out_file = open(os.getcwd() + '/encrypted.txt', 'w')
    out_file.write(ciphertext)
    out_file.close()
    print('File encrypted successfully. ("encrypted.txt" created)')


########
# MAIN #
########
if __name__ == "__main__":
    #check for correct usage
    if len(sys.argv) < 2 or sys.argv[1] not in ['decrypt', 'encrypt', 'hint']:
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
