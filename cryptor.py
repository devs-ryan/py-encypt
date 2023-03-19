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
    print('  Flags:')
    print('    --ignore-path')
    print('      (Will use the current working directory instead of typical file path)')
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

####################
# PRINT FILES LIST #
####################
def getPath():
    ignorepath = '--ignore-path' in sys.argv or '-i' in sys.argv
    return FILE_PATH if (not ignorepath and FILE_PATH and FILE_PATH != '') else os.getcwd()


###################
# Get File Choice #
###################
def getFileChoice():
    filepath = getPath() 
    files_in_path = sorted([f for f in os.listdir(filepath) if os.path.isfile(os.path.join(filepath, f))])

    #print files in path list / ID
    for index, file in enumerate(files_in_path):
        print('['+ str(index) +'] - ' + file)

    #get user input    
    filename = input("Enter file name: ")

    #convert index entries to string filename
    if filename.isdigit() and int(filename) < len(files_in_path):
        filename = files_in_path[int(filename)]
        print('Selected: ' + filename)

    return {
        'full': filepath + '/' + filename,
        'path': filepath,
        'name': filename
    }


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
    file_choice = getFileChoice()
    #read file
    try:
        data_file = open(file_choice['full'], 'r')
    except FileNotFoundError:
        print("File not found in " + file_choice['full'])
        sys.exit()
        
    file_contents = data_file.read()
    
    #decypt file contents
    text = decryptTxt(getpass.getpass("Enter a password: "), file_contents)
    if '--output' in sys.argv or '-o' in sys.argv:
        out_filename = input("Specify output file name: ")
        if out_filename == '':
            out_filename = 'decrypted.txt'

        out_file = open(os.getcwd() + '/' + out_filename, 'w')
        out_file.write(text.decode('utf-8'))
        out_file.close()
        print('File decrypted successfully. ("' + out_filename + '" created in current working directory)')
    else:
        print(text.decode('utf-8'))
        print('File decrypted successfully.')


###########
# ENCRYPT #
###########
def encryptProcedure():
    file_choice = getFileChoice()
    #read file
    try:
        data_file = open(file_choice['full'], 'r')
    except FileNotFoundError:
        print("File not found in working directory")
        sys.exit()
    
    file_contents = data_file.read()
    #encrypt file contents
    ciphertext = encryptTxt(getpass.getpass("Enter a password: "), file_contents)
    
    #print cipher text to file
    encrypt_filename = input("Specify encrypted file name: ")
    if encrypt_filename == '':
        encrypt_filename = 'encrypted.txt'

    out_file = open(encrypt_filename, 'w')
    out_file.write(ciphertext)
    out_file.close()
    print('File encrypted successfully. ("' + encrypt_filename + '" created)')


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
