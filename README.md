# Password-Locker
Simple Password locker automation with python made by deadcode

Made By Deadcode (DeadIV or vLogix)

## Requirements

```
sys
```
```
pyperclip
```

## Licesnse

  **MIT**

## Explanation

First add libraries

```
import sys,pyperclip
```

then add 'PASSWORDS' and simple argv reader

```
PASSWORDS = {'email':'tryrt435@#$@#','blog':'tretertrt@$#!@','luggage':'5234134#@#'}

if len(sys.argv) < 2:
    print('Usage: python main.py [account] - copy account password')
    sys.exit()
```

Finally add copy & paste to clipboard

```
account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print("There's no account named " + account)
```

## Author

**Deadcode (DeadIV or vLogix)**
