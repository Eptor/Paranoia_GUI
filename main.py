import PySimpleGUI as sg
from defs.crypto_defs import encrypt as enc
from defs.crypto_defs import decrypt as dec
from os import path
from datetime import date
from pathlib import Path

password = ''  # Change the value to the password you want to use
base = 'img/View.ico'  # Icon location

# -- -- -- -- -- -- -- -- -- -- -- -- -- GUI DEFINITION -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- #
# Add a touch of color
sg.theme('DarkGrey6')
# All the stuff inside your window.
layout = [  [sg.FileBrowse('Encrypt:', target='FileName_encrypt'), sg.Input(key='FileName_encrypt')],
            [sg.FileBrowse('Decrypt:', target='FileName_decrypt'), sg.Input(key='FileName_decrypt')],
            [sg.Button('Next'), sg.Button('Cancel')]
]

sg.set_global_icon(base)

# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- #

# Create the Window
window = sg.Window('Paranoia', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event not in (None, 'Cancel') and values['FileName_encrypt'] != '' and values['FileName_decrypt'] == '':
        token = enc(Path(values['FileName_encrypt']), password)  # Gets the encrypted data from the file given on the file browser
        output = sg.popup_get_folder('Select your output', title='Output', icon='img/Folder.ico')  # Gets the choosen ouput folder
        with open(path.join(output, f'{date.today()}.cryptic'), 'wb') as encryption:
            encryption.write(token)  # Writes the data on the encrypted file
        sg.popup_ok('Encryption succesfull', title='Done!')
        window['FileName_encrypt']('')  # Clean the window

    elif event not in (None, 'Cancel') and values['FileName_encrypt'] == '' and values['FileName_decrypt'] != '':
        end_name = sg.popup_get_text('Enter the new file name:', title='File Name', icon='img/Rename.ico')  # Gets the name for the new file
        output = sg.popup_get_folder('Select yout output', title='Output', icon='img/Folder.ico')  # Gets the choosen ouput folder
        token = dec(Path(values['FileName_decrypt']), password)  # Gets the decrypted data
        with open(path.join(output, end_name), 'wb') as decryption:
            decryption.write(token)  # Writes the data on the new file
        sg.popup_ok('Decryption succesfull', title='Done!')
        window['FileName_decrypt']('')  # Clean the window

    elif event not in (None, 'Cancel') and values['FileName_encrypt'] == '' and values['FileName_decrypt'] == '':
        sg.popup_ok('You need to input a file')  # When no file is given, this error raise

    elif event in (None, 'Cancel'):
        break  # Breaks the loop - closes the window 

window.close()
