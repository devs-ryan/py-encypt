#!/usr/local/bin/python3
import sys
from base64 import b64encode, b64decode
from simplecrypt import encrypt, decrypt

def usage():
    print('===================')
    print('=====Py-Encypt=====')
    print('===================')
    print('Usage:')
    print('  ./cryptor.py [option] [flag]')
    print('Options:')
    print('  ------------')
    print('  [1] Encypt:')
    print('  ------------')
    print('  Flag = encrypt')
    print('  Description: Encrypts a file')
    print('  Flags: N/A')
    print('  ------------')
    print('  [2] Decrypt:')
    print('  ------------')
    print('  Flag = decrypt')
    print('  Description: Decrypts a file')
    print('  Flags:')
    print('    --output')
    print('      (Will request an output file name rather than printing to terminal)')

def encryptTxt(password, txt):
    ciphertext = encrypt(password, txt)
    return b64encode(ciphertext).decode('utf-8')

def decryptTxt(password, ciphertext):
    decoded_ciphertext = b64decode(ciphertext)
    return decrypt(password, decoded_ciphertext)

def decryptProcedure():
    filepath = input("Enter file name or path: ")
    data_file = open(filepath,'r')
    file_contents = data_file.read()
    #decypt file contents
    text = decryptTxt(input("Enter a password: "), file_contents)
    if len(sys.argv) > 2 and sys.argv[2] == '--output':
        out_file = open('decrypted.txt', 'w')
        out_file.write(text.decode('utf-8'))
        out_file.close()
        print('File decypted successfully. ("decrypted.txt" created)')
    else:
        print(text.decode('utf-8'))
        print('File decypted successfully.')


def encryptProcedure():
    filepath = input("Enter file name or path: ")
    #read file
    data_file = open(filepath,'r')
    file_contents = data_file.read()
    #encypt file contents
    ciphertext = encryptTxt(input("Enter a password: "), file_contents)
    #print cipher text to file
    out_file = open('encrypted.txt', 'w')
    out_file.write(ciphertext)
    out_file.close()
    print('File encypted successfully. ("encrypted.txt" created)')


if __name__ == "__main__":
    #check for correct usage
    if len(sys.argv) < 2 or (sys.argv[1] != 'encrypt' and sys.argv[1] != 'decrypt'):
        usage()
        sys.exit()
    #decrypt
    if sys.argv[1] == 'decrypt':
        print('decrypting...')
        decryptProcedure()

    else:
        print('encrypting...')
        encryptProcedure()


