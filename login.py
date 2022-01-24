import PySimpleGUI as sg
import webbrowser

#make sure path to firefox is created
firefox_path="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(firefox_path))

#Layout
loginInfo = [[sg.Text('Username to Enter', size = (15,1)), sg.InputText()], [sg.Text('Password to Enter', size =(15,1)), sg.InputText()], [sg.Button('Submit Login Info')]]
websitesInfo = [[sg.Button('Login to Galaxy')], [sg.Button('Login to Elearning')], [sg.Button('Login to All')]]
layout = [[sg.Column(loginInfo, element_justification='c'), sg.Column(websitesInfo, element_justification='c')]]
# Create the window
window = sg.Window("Python Login", layout, margins=(100,20))

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window 
    if event == sg.WIN_CLOSED:
        break
    if event == 'Login to Elearning' or event == 'Login to All':
        
        webbrowser.get('firefox').open('elearning.utdallas.edu/')
    if event == 'Login to Galaxy' or event == 'Login to All':
        webbrowser.get('firefox').open('https://www.utdallas.edu/galaxy/')

window.close()