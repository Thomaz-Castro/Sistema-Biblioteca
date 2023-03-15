import PySimpleGUI as sg
import pandas as pd
import sql

con = sql.criar_conexao("localhost", "root", "", "biblioteca")
query = """select u.nome, l.titulo, empr.data_emprestimo from emprestimos as empr
join usuarios as u
on u.id = empr.usuario_id
join livros as l
on l.id = empr.livro_id;"""
df = pd.read_sql(query, con)

# Definindo o layout
sg.theme('DarkBlue17')
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
        [sg.Button('PESQUISAR', size=(17, 3), button_color=('white', 'darkblue')),sg.Button('ADICIONAR', size=(17, 3), button_color=('white', 'green')), sg.Button('OPÇÕES', size=(17, 3), button_color=('black', 'darkgray'))]
    ], element_justification='center', expand_x=True)],
    [sg.Column([
    [sg.Column([
        [sg.Table(values=df.values.tolist(), headings=df.columns.tolist(), auto_size_columns=True,
                  justification='center', num_rows=min(25, len(df)))],
    ], element_justification='center', expand_x=True, pad=(20, 0))],
], element_justification='center', expand_x=True, pad=(20, 0))],
[sg.Column([    [sg.Text('Campo 1', size=(10, 1), justification='left'),      sg.Text('Campo 2', size=(10, 1), justification='right', pad=((400, 20), 0))],
], element_justification='center', expand_x=True, pad=(100, 0))]

]



# Criando a janela
janela = sg.Window('Sistema Biblioteca', layout_column, size=(832, 468))

# Loop de eventos
while True:
    evento, valores = janela.read()
    
    if evento == sg.WINDOW_CLOSED:
        break
        
    # Exemplo de como atualizar a tabela com dados do pandas
    if evento == 'ADICIONAR':
        import pandas as pd
        df = pd.DataFrame({'id_usuario': ['001', '002', '003'],
                           'id_livro': ['0001', '0002', '0003'],
                           'data_emprestimo': ['01/01/2022', '02/01/2022', '03/01/2022'],
                           'data_devolucao': ['08/01/2022', '09/01/2022', '10/01/2022']})
        
        # Atualiza a tabela com os dados do df
        janela['-TABLE-'].update(values=df.values.tolist(), headings=df.columns.tolist())
    
    # Exemplo de como alterar o texto dos campos de texto
    if evento == 'PESQUISAR':
        janela['-LEFT-'].update('Resultado da pesquisa:')
        janela['-RIGHT-'].update('Mais informações aqui.')
        
# Fechando a janela
janela.close()
