# py-encypt
python text file encypt / decypt progam <br>
Place this script in your path for easy access to encrypt/decrypt text files.

Setup:
======
* Requires python3
* Update path to python3 at top of script if nessesary
* pip3 install simple-crypt
* pip3 uninstall PyCrypto && pip3 install -U PyCryptodome

Optional:
======
* set APP_KEY='{Your App Key}' inside script to a local KEY that will be appended to encryption passwords for extra security.
* set PASSWORD_HINT='{Your PW Hint}' inside script that will be shown with the "hint" option.
* set FILE_PATH='{Your File Path}' inside script to use as file path when decypting files to the terminal.

Usage:
======
  cryptor.py [option] [flags]

Options:
========
#### [1] Encypt:
* Option = encrypt
* Description: Encrypts a file
* Flags: N/A
  
#### [2] Decrypt:
* Option = decrypt
* Description: Decrypts a file
* Flags:

    --output
      (Will output to file rather than printing to terminal)
      
    --ignore-path
      (Will use the current working directory instead of typical file path)
      
#### [3] Hint:
* Option = hint
* Displays password hint
