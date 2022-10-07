import PySimpleGUI as sg
from copiar import calc

crivo = ''
sg.theme('DarkAmber')

layout = [
    [sg.FileBrowse('Select model', key='buscar_crivo'), sg.Text('File: ', key='crivo')],
    [sg.HorizontalSeparator()],
    [sg.FileBrowse('Select .mpc file', key='buscar_mpc'), sg.Text('File: ', key='mpc')],
    [sg.HorizontalSeparator()],
    [sg.Checkbox('Receive data on the same line?', key='linha')],
    [sg.Button('Copy data', key='botao_buscar'), sg.Checkbox('Comma?', key='virgula')],
]

window = sg.Window('MedPC to Excel', layout, size=(600, 200))

while True:
    event, value = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == 'botao_buscar':
        print(value)
        crivo = open(value['buscar_crivo'])
        arquivo = open(value['buscar_mpc'])
        linha = value['linha']
        sg.PopupOK(calc(arquivo, crivo, linha, value['virgula']))
        arquivo.close()
        crivo.close()
window.close()

