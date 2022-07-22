from PySimpleGUI import Window, Button, Text, Input, FileBrowse, Checkbox, InputText, theme
from Copiar import copiar
import json

try:
    arquivo = open('config.json')
    crivo = json.load(arquivo)
    arquivo.close()
except:
    arquivo = {"inicio": "", "final": "", "indices": ""}
    crivo = arquivo

layout = [
    [],
    [Text("Selecione o arquivo", key='-ARQUIVO-'), Input(key='-FILE-', visible=False, enable_events=True), FileBrowse('Encontrar Arquivo')],
    [Text('Onde inicia os dados?'), InputText(crivo['inicio'], key='-INICIO-')],
    [Text('Onde termina os dados?'), InputText(crivo['final'], key='-FINAL-')],
    [Text('Digite os index separados pro vírgula'), InputText(crivo['indices'], key='-INDICES-')],
    [Checkbox('Selecionar todos os dados? ', key='-LISTA-')],
    [Button('Copiar', key='-COPIAR-')],
]

theme('Material1')

window = Window(
    'MedToExcel - by Fábio Henrique',
    size=(400, 400),
    layout=layout
)

while True:
    event, values = window.read()

    match event:
        case '-FILE-':
            pass
        case None:
            break
        case '-COPIAR-':
            dados = copiar(
                values['-FILE-'],
                values['-INICIO-'],
                values['-FINAL-'],
                values['-INDICES-'],
                values['-LISTA-']
            )
            crivo = {
                'inicio': values['-INICIO-'],
                'final': values['-FINAL-'],
                'indices': values['-INDICES-']
            }
            arquivo = open('config.json', 'w')
            json.dump(crivo, arquivo)
            arquivo.close()
window.close()
