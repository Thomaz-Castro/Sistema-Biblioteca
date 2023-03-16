import PySimpleGUI as sg
import pandas as pd
import sql

con = sql.criar_conexao("localhost", "root", "", "biblioteca")
query = """select u.nome, l.titulo, aut.nome, edit.nome,l.isbn , empr.data_emprestimo, empr.data_devolucao  from emprestimos as empr
join usuarios as u
on u.id = empr.usuario_id
join livros as l
on l.id = empr.livro_id
join autores as aut
on aut.id = l.autor_id
join editoras as edit
on edit.id = l.editora_id
order by empr.id desc"""
df = pd.read_sql(query, con)
colunas = ['Usuario', 'Livro', 'Autor', 'Editora', 'ISBN', 'Empréstimo', 'Devolução']

# Definindo o layout

sg.theme('DarkTeal9')
con = sql.criar_conexao("localhost", "root", "", "biblioteca")
colunas = ['Usuario', 'Livro', 'Autor', 'Editora', 'ISBN', 'Empréstimo', 'Devolução']
df = pd.read_sql("""select u.nome, l.titulo, aut.nome, edit.nome,l.isbn , empr.data_emprestimo, empr.data_devolucao  from emprestimos as empr join usuarios as u on u.id = empr.usuario_id join livros as l on l.id = empr.livro_id join autores as aut on aut.id = l.autor_id join editoras as edit on edit.id = l.editora_id order by empr.id desc""", con)
layout_column = [
    [sg.Text('📚 Sistema Biblioteca 📚', font=('arial', 36), justification='center', expand_x=True)],
    [sg.Column([
        [sg.Text('id usuário      ', font=('Helvetica', 13), tooltip='Digite o ID do usuário:'),
        sg.Text('id livro           ', font=('Helvetica', 13), tooltip='Digite o ID do livro:'),
        sg.Text('data de emprestimo                      ', font=('Helvetica', 13), tooltip='Data = dd/mm/aaaa ou aaaa/mm/dd'),
        sg.Text('data de devolução                      ', font=('Helvetica', 13), tooltip='Data = dd/mm/aaaa ou aaaa/mm/dd')],
        [sg.Input(key='id-usuario', size=(15)), sg.Input(key='id-livro', size=(15)),
        sg.Input(key='data-empr', size=(36)), sg.Input(key='data-devol', size=(36))]
    ], element_justification='center', expand_x=True, pad=(20, 0))],
    [sg.Column([
        [sg.Button('PESQUISAR 🔎', size=(17, 3), button_color=('white', 'darkblue')),sg.Button('ADICIONAR ➕', size=(17, 3), button_color=('white', 'green')), sg.Button('OPÇÕES ⚙️', size=(17, 3), button_color=('black', 'darkgray'))]
    ], element_justification='center', expand_x=True, pad=(0,7))],
    [sg.Column([
    [sg.Column([
        [sg.Table(values=df.values.tolist(), headings=colunas, auto_size_columns=True,
                justification='center', num_rows=13, key='-TABLE-')],
    ], element_justification='center', expand_x=True, pad=(20, 10))],
], element_justification='center', expand_x=True, pad=(20, 0))],
[sg.Column([    [sg.Text('*mensagem', size=(30, 1), justification='left', key=('-MSG-')),      sg.Text('Status Servidor: ON', key='-StsSer-' , size=(20, 1), justification='right', pad=((300, 20), 0))],
], element_justification='center', expand_x=True, pad=(100, 0))],
[sg.Text("Software desenvolvido por Thomaz Castro", justification='center', expand_x=True, pad=(10,20))]
]

janela = sg.Window('Sistema Biblioteca', layout_column, size=(1024, 576))

""" sg.theme('DarkTeal9')
layout=[
    [sg.Text('Pesquisar🔎', font=('arial', 48))],
    [sg.Button('Usuários 🧑', font=('arial', 32), size=(13, 2)),
     sg.Button('Livros 📕', font=('arial', 32), size=(13, 2))],
    [sg.Button('     Autores ✍️', font=('arial', 32), size=(13, 2)),
     sg.Button('Editoras 🏢', font=('arial', 32), size=(13, 2))],
     [sg.Button('Voltar', font=('arial', 32), size=(15, 1), button_color=('white', 'red'), border_width=5, pad=(10,70))]
]
janela = sg.Window('Pesquisar🔎', layout, element_justification='c', size=(1024, 576)) """

# Loop de eventos
while True:
    evento, valores = janela.read()

    if evento == sg.WINDOW_CLOSED:
        break

    # Exemplo de como atualizar a tabela com dados do pandas
"""     if evento == 'ADICIONAR ➕':
        sql.insere_emprestimo(con, str((valores['id-usuario'])),str((valores['id-livro'])),str((valores['data-empr'])),str((valores['data-devol'])))
        df = pd.read_sql(query, con)
        # Atualiza a tabela com os dados do df
        janela['-TABLE-'].update(values=df.values.tolist()) """

    # Exemplo de como alterar o texto dos campos de texto
# Fechando a janela
janela.close()
