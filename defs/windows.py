import PySimpleGUI as sg
from defs.crypto_defs import encrypt as enc
from defs.crypto_defs import decrypt as dec
from os import path
from datetime import date
from pathlib import Path
from time import sleep as s
import pyperclip

password = 'pedro'  # Change the value to the password you want to use
base = 'img/View.ico'  # Icon location

# -- -- -- -- -- -- -- -- -- -- -- -- -- GUI DEFINITION -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- #
# Add a touch of color
sg.theme('DarkGrey6')
# All the stuff inside your window.

main = [
    [sg.Button('File', key='File'), sg.Button('Cancel')]
]

sg.set_global_icon(base)

# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- #

def file_mode():

    '''
    Handles all related to the files window
    '''

    file = [  
        [sg.FileBrowse('Encrypt:', target='FileName_encrypt'), sg.Input(key='FileName_encrypt')],
        [sg.FileBrowse('Decrypt:', target='FileName_decrypt'), sg.Input(key='FileName_decrypt')],
        [sg.Button('Next'), sg.Button('Cancel')]
    ]

    window = sg.Window('Paranoia', file,)
    
    event, values = window.read()

    while True:

        if event in (None, 'Cancel'):
            window.close()
            break

        elif values['FileName_encrypt'] != '' and values['FileName_decrypt'] == '':
            token = enc('file', Path(values['FileName_encrypt']), password)  # Gets the encrypted data from the file given on the file browser
            output = sg.popup_get_folder('Select your output', title='Output', icon='img/Folder.ico')  # Gets the choosen ouput folder
            with open(path.join(output, f'{date.today()}.cryptic'), 'wb') as encryption:
                encryption.write(token)  # Writes the data on the encrypted file
            sg.popup_ok('Encryption succesfull', title='Done!')
            window.close()
            break

        elif values['FileName_encrypt'] == '' and values['FileName_decrypt'] != '':
            end_name = sg.popup_get_text('Enter the new file name:', title='File Name', icon='img/Rename.ico')  # Gets the name for the new file
            output = sg.popup_get_folder('Select yout output', title='Output', icon='img/Folder.ico')  # Gets the choosen ouput folder
            token = dec('file' ,Path(values['FileName_decrypt']), password)  # Gets the decrypted data
            with open(path.join(output, end_name), 'wb') as decryption:
                decryption.write(token)  # Writes the data on the new file
            sg.popup_ok('Decryption succesfull', title='Done!')
            window.close()
            break

        elif event == 'Next' and values['FileName_encrypt'] == '' and values['FileName_decrypt'] == '':
            sg.popup_ok('You need to input a file')  # When no file is given, this error raise


def text_mode():

    '''
    Handles all related to the text mode
    '''

    texts = [
        [sg.Input(key='data')],
        [sg.Button('Encrypt', key='Encrypt'), sg.Button('Decrypt', key='Decrypt'), sg.Button('Cancel', key='Cancel')]
    ]

    window = sg.Window('Paranoia', texts)

    event, values = window.read()


    while True:
        if event in (None, 'Cancel'):
            window.close()
            break
            
        elif event == 'Encrypt':
            token = enc('text', values['data'].encode(), password)
            pyperclip.copy(token.decode())
            sg.popup_no_wait('Copied', token.decode())
            window.close()
            break

        elif event == 'Decrypt':
            token = dec('text', values['data'].encode(), password)
            pyperclip.copy(token.decode())
            sg.popup_no_wait('Copied', token.decode())
            window.close()
            break

        else:
            print('help')
