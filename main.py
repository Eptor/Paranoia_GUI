import PySimpleGUI as sg
from defs.windows import file_mode as files
from defs.windows import text_mode as text

base = 'img/View.ico'  # Icon location

# -- -- -- -- -- -- -- -- -- -- -- -- -- GUI DEFINITION -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- #
# Add a touch of color
sg.theme('DarkGrey6')

# All the stuff inside your window.
main = [
    [sg.Button('File', key='File'), sg.Button('Text', key='Text'), sg.Cancel()]
]

sg.set_global_icon(base)

# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- #

# Create the main Window
window_main = sg.Window('Paranoia', main)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window_main.read()

    if event in (None, 'Cancel'):
        break  # Breaks the loop - closes the window 

    else:
        if event == 'File':
            window_main.disappear()  # hide main window
            files()
            window_main.reappear()  # reappears the main window
        
        elif event == 'Text':
            window_main.disappear()
            text()
            window_main.reappear()

window_main.close()
