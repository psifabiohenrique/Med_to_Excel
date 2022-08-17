import PySimpleGUI as sg
from copiar import calc

crivo = ''
sg.theme('DarkAmber')

layout = [
    [sg.FileBrowse('Selecionar o crivo!', key='buscar_crivo'), sg.Text('Arquivo: ', key='crivo')],
    [sg.HorizontalSeparator()],
    [sg.FileBrowse('Selecionar o MPC!', key='buscar_mpc'), sg.Text('Arquivo: ', key='mpc')],
    [sg.HorizontalSeparator()],
    [sg.Checkbox('Receber dados na mesma linha?', key='linha')],
    [sg.Button('Copiar Dados', key='botao_buscar'), sg.Checkbox('Virgula?', key='virgula')],
]

window = sg.Window('MedPC para Excel', layout, size=(600, 200))

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

