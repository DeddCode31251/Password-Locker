# An insecure password locker program
# Made by Deadcode (DeadIV or Vlogix)

import sys,pyperclip

PASSWORDS = {'email':'tryrt435@#$@#','blog':'tretertrt@$#!@','luggage':'5234134#@#'}



if len(sys.argv) < 2:
    print('Usage: python main.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line is the account name 

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print("There's no account named " + account)
