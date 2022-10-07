# Nome do meu projeto

Rápida descrição do objetivo de fazer esse projeto

| :placard: Vitrine.Dev |     |
| -------------  | --- |
| :sparkles: Nome        | **.mpc file converter for excel**
| :label: Tecnologias | Python

<!-- Inserir imagem com a #vitrinedev ao final do link -->
![](https://github.com/psifabiohenrique/Med_to_Excel/blob/main/imagem_programa.png?raw=true#vitrinedev)

## Project details

This project was developed so that behavior analysts can extract data from MedPc-generated .mpc files for spreadsheets (excel, libreOffice...).

To use you can clone the repository and generate an executable.

The model is a .txt file containing the data you want to extract. In this file you must put the DIM and the index separated by "-". Each line of the txt file must have only one pair of DIM and index. The example_model.txt file is an example of how this file should be arranged.

If you want to get all the values within the same DIM, you can create a sieve containing only the DIM followed by "-FULL".
By default, the program copies the data arranged in a single column to the system's clipboard. If you want to receive the data in a single line, check the option "Receive data on the same line?".
In Brazil, the standard is to use the comma as a decimal separator, but the program by default copies the values using the period as a separator. Check the "comma?" to receive the data separating the decimals by a comma.

## Detalhes do projeto | 

Este projeto foi desenvolvido para que analistas do comportamento possam extrair os dados dos arquivos .mpc gerados pelo MedPc para planilhas (excel, libreOffice...).

Para utilizar você pode clonar o repositório e gerar um executável.

O modelo é um arquivo .txt contendo os dados que deseja extrair. Nesse arquivo você deverá colocar o DIM e o indice separados por "-". Cada linha do arquivo txt deverá ter somente um par de DIM e indice. O arquivo exemple_model.txt é um exemplo de como esse arquivo deve estar disposto.

Caso queira pegar todos os valores dentro de um mesmo DIM, você pode criar um crivo contendo somente o DIM seguido por "-FULL".
Por padrão o programa copia para a área de transferência do sistema os dados dispostos em uma única coluna, caso queira receber os dados em uma única linha, marque a opção "Receive data on the same line?".
No Brasil o padrão é utilizar a virgula como separador decimal, porém o programa por padrão copia os valores utilizando o ponto como separador. Marque a opção "comma?" para receber os dados separando os decimais por vírgula.
