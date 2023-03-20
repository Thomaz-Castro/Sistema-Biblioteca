import PySimpleGUI as sg
from pandas import read_sql
from sql import criar_conexao


def Janela_Inicio():
    sg.theme('DarkTeal9')
    con = criar_conexao("localhost", "root", "", "biblioteca")
    colunas = ['Usuario', 'Livro', 'Autor', 'Editora', 'ISBN', 'Empréstimo', 'Devolução']
    df = read_sql("""select u.nome, l.titulo, aut.nome, edit.nome,l.isbn , empr.data_emprestimo, empr.data_devolucao  from emprestimos as empr join usuarios as u on u.id = empr.usuario_id join livros as l on l.id = empr.livro_id join autores as aut on aut.id = l.autor_id join editoras as edit on edit.id = l.editora_id order by empr.id desc""", con)
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
    [sg.Column([    [sg.Text('*mensagem', size=(50, 1), justification='left', key=('-MSG-')),      sg.Text('Servidor: ON', key='-StsSer-' , size=(20, 1), justification='right', pad=((280, 20), 0))],
    ], element_justification='center', expand_x=True, pad=(100, 0))],
    [sg.Text("Software desenvolvido por Thomaz Castro", justification='center', expand_x=True, pad=(10,20))]
    ]

    return sg.Window('Sistema Biblioteca', layout_column, size=(1024, 576), finalize=True)

def janela_pesquisa():
    sg.theme('DarkTeal9')
    layout=[
        [sg.Text('Pesquisar🔎', font=('arial', 48))],
        [sg.Button('Usuários 🧑', font=('arial', 32), size=(13, 2)),
        sg.Button('Livros 📕', font=('arial', 32), size=(13, 2))],
        [sg.Button('     Autores ✍️', font=('arial', 32), size=(13, 2)),
        sg.Button('Editoras 🏢', font=('arial', 32), size=(13, 2))],
        [sg.Button('Voltar', font=('arial', 32), size=(15, 1), button_color=('white', 'red'), border_width=5, pad=(10,70))]
    ]
    return sg.Window('Pesquisar🔎', layout, element_justification='c', size=(1024, 576), finalize=True)

def pesquisa_usuario():
    sg.theme('DarkTeal9')
    con = criar_conexao("localhost", "root", "", "biblioteca")
    df = read_sql("select * from usuarios;",con)
    colunas_pes_usu=['ID','Nome', 'Endereço','Cidade','UF','Sexo','Telefone','Email']
    layout = [
        [sg.Text('Usuários 🧑', font=('arial', 48))],
        [sg.Column([
            [sg.Text('ID      ', font=('Helvetica', 10), tooltip='Digite o ID do usuário:'),
            sg.Text('Nome                  ', font=('Helvetica', 13), tooltip='Digite o nome do usuário:'), sg.Text('Endereço                                   ', font=('Helvetica', 13), tooltip='Digite o endereço do usuário:')],
            [sg.Input(key='id-usuario', size=(5)), sg.Input(key='usuario-nome',
                                                            size=(17)), sg.Input(key='usuario-ender', size=(36))]
        ], element_justification='center', expand_x=True, pad=(285, 0))],
        [sg.Column([
            [sg.Text('Cidade                                        ', font=('Helvetica', 13), tooltip='Digite o ID do usuário:'),
            sg.Text('UF        ', font=('Helvetica', 10), tooltip='Digite o UF da cidade:'), sg.Text('Sexo         ', font=('Helvetica', 11), tooltip='Digite o sexo do usuario:')],
            [sg.Input(key='cidade-usuario', size=(36)), sg.Combo(values=['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE',
                                                                        'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'], key='usuario-UF', size=(5)), sg.Combo(key="usuario-Sexo", size=(15), values=["Homem", "Mulher"])]
        ], element_justification='left', expand_x=True, pad=(285, 0))],
        [sg.Column([
            [sg.Text('Email                                             ', font=('Helvetica', 10), tooltip='Digite o email do usuário:'),
            sg.Text('Telefone (só numeros)', font=('Helvetica', 10), tooltip='Digite o telefone do usuário')],
            [sg.Input(key='telefone-usuario', size=(30)),
            sg.Input(key='email-usuario', size=(30))]
        ], element_justification='left', expand_x=True, pad=(285, 0))],
        [sg.Button("pesquisar", expand_x=True, pad=(285, 20))],
        [sg.Column([
            [sg.Table(values=df.values.tolist(), headings=colunas_pes_usu, auto_size_columns=True,
                        justification='center', num_rows=7, key='-TABLE-')],
        ], element_justification='center', expand_x=True)],
        [sg.Button('Voltar', font=('arial', 32), size=(15, 1),
                button_color=('white', 'red'), border_width=5, pad=(10, 20))]
    ]
    return sg.Window('Pesquisar🔎', layout, element_justification='c', size=(1024, 576), finalize=True)


