# py-encypt
python text file encypt / decypt progam
Place this script in your file path for easy access to encrypt/decrypt text files.

Optional:
======
* set APP_KEY='{Your App Key}' inside script to a local KEY that will be appended to encryption passwords for extra security.
* set PASSWORD_HINT='{Your PW Hint}' inside script that will be shown with the "hint" option.

Usage:
======
* cryptor.py {option} {flag}

Options
------
#### [1] Encypt:
* Option = encrypt
* Description: Encrypts a file
* Flags: N/A
  
#### [2] Decrypt:
* Option = decrypt
* Description: Decrypts a file
* Flags:
    --output
      (Will request an output file rather than printing to terminal)
      
#### [3] Hint:
* Option = hint
* Displays password hint
