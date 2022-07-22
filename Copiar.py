import pyperclip as pc
from PySimpleGUI import popup, theme_previewer


def copiar(arquivo_bruto, inicio, fim, string_indices, lista):

    pdc = False
    try:
        arquivo = open(arquivo_bruto)
    except:
        return 'Não foi possível abrir o arquivo'

    indices_temp = string_indices.split(',')

    indices = []
    for i in indices_temp:
        indices.append(int(i))

    dados = []
    for i in arquivo:
        if f'{inicio}:\n' in i:
            pdc = True
        if f'{fim}:\n' in i:
            pdc = False
        if pdc:
            temp = i.split()
            temp.pop(0)
            for ii in temp:
                dados.append(ii)

    dados_para_copiar = ''
    if lista:
        for i in dados:
            dados_para_copiar += f'{i} '
    elif len(indices) > 1:
        for i in indices:
            try:
                dados_para_copiar += f'{dados[i]} '
            except:
                return 'Não foi possível encontrar os dados'
    else:
        dados_para_copiar = dados[indices[0]]

    dados_para_copiar = dados_para_copiar.replace('.', ',')
    pc.copy(dados_para_copiar)
    popup('Copiado')
    return 'Copiado'
