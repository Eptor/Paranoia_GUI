# GUI for Paranoia

A GUI for the repo <a href="https://github.com/Eptor/Paranoia">Paranoia</a>

## Salt
You can change the salt used by the functions, just use the os module:
```
os.urandom(16)
```
and change the salt value on Defs/crypto_defs.py

## Install

You can use:
```
pip install -r requirements.txt -y 
```

or install the modules individually

Cryptogrphy module:

```
pip install cryptography
```

Pyperclip module (only windows for now):

```
pip install pyperclip
```

And for the GUI you will need the PySimpleGui module:

```
pip install PySimpleGUI
```

GUI icons by <a href="https://iconscout.com/contributors/nixxdsgn">NIXX Design</a> on <a href="https://iconscout.com">Iconscout</a>
