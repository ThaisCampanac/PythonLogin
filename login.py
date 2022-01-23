from tkinter.tix import Tree
import PySimpleGUI as sg
import webbrowser

#webbrowser.register('firefox', webbrowser.BackgroundBrowser('firefox'), preferred=True)
#webbrowser.get('firefox')

urL='https://www.python.org'
mozilla_path="C:\\Program Files\\Mozilla Firefox"
webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(mozilla_path))
webbrowser.get('firefox')
print (webbrowser._browsers)
#Layout
layout = [[sg.Button('Login to Galaxy')], [sg.Button('Login to Elearning')], [sg.Button('Login to All')]]
# Create the window
window = sg.Window("Python Login", layout, margins=(100,20))
# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == sg.WIN_CLOSED:
        break
    if event == 'Login to Elearning' or event == 'Login to All':
        webbrowser.get('firefox').open('elearning.utdallas.edu/')

window.close()