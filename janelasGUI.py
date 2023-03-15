import PySimpleGUI as sg
""" 

layout_column = [
    [sg.Text('📚 Sistema Biblioteca 📚', font=('arial', 36))],
    [sg.Text('id usuário      ', font=('Helvetica', 13), tooltip='Digite o ID do usuário:'), sg.Text('id livro           ', font=('Helvetica', 13), tooltip='Digite o ID do livro:'), sg.Text(
        'data de emprestimo                      ', font=('Helvetica', 13), tooltip='Data = dd/mm/aaaa ou aaaa/mm/dd'), sg.Text('data de devolução                      ', font=('Helvetica', 13), tooltip='Data = dd/mm/aaaa ou aaaa/mm/dd')],
    [sg.Input(key='id-usuario', size=(15)), sg.Input(key='id-livro', size=(15)),sg.Input(key='data-empr', size=(36)), sg.Input(key='data-devol', size=(36))],
    [sg.Button('PESQUISAR', size=(17, 3), button_color=('white', 'darkblue')), sg.Button('ADICIONAR', size=(17, 3),button_color=('white', 'green')), sg.Button('OPÇÕES', size=(17, 3),button_color=('black', 'darkgray'))],

]

layout = [
    [sg.Column(layout_column, element_justification='c', justification='c')]]

janela = sg.Window('Video Downloader', layout, size=(832, 468)) """

layout = [
    [sg.Text('📚 Sistema Biblioteca 📚', font=('arial', 36))],
    [sg.Text('id usuário      ', font=('Helvetica', 13), tooltip='Digite o ID do usuário:'), sg.Text('id livro           ', font=('Helvetica', 13), tooltip='Digite o ID do livro:'), sg.Text(
        'data de emprestimo                      ', font=('Helvetica', 13), tooltip='Data = dd/mm/aaaa ou aaaa/mm/dd'), sg.Text('data de devolução                      ', font=('Helvetica', 13), tooltip='Data = dd/mm/aaaa ou aaaa/mm/dd')],
    [sg.Input(key='id-usuario', size=(15)), sg.Input(key='id-livro', size=(15)),sg.Input(key='data-empr', size=(36)), sg.Input(key='data-devol', size=(36))],
    [sg.Button('PESQUISAR', size=(17, 3), button_color=('white', 'darkblue')), sg.Button('ADICIONAR', size=(17, 3),button_color=('white', 'green')), sg.Button('OPÇÕES', size=(17, 3),button_color=('black', 'darkgray'))],
    [sg.Table(values=[], headings=[], max_col_width=25, auto_size_columns=True,
              justification='center', num_rows=10, alternating_row_color='lightblue',
              key='-TABLE-', tooltip='Dados da tabela')],
    [sg.Input(key='-LEFT-', size=(20,1)), sg.Input(key='-RIGHT-', size=(20,1))],
]

# Criando a janela
janela = sg.Window('Sistema Biblioteca', layout)

# Criar a janela e os elementos
# ...


while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
