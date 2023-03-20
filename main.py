import PySimpleGUI as sg
import janelasGUI as gui
import sql
from pandas import read_sql
""" from dateutil import parser """

""" def is_valid_date(date_string):
    try:
        parser.parse(date_string)
        return True
    except ValueError:
        return False

def extract_date_parts(date_string):
    try:
        date = parser.parse(date_string)
        year, month, day = date.year, date.month, date.day
        return year, month, day
    except ValueError:
        return None, None, None """


#Conectar ao banco de dados
con = sql.criar_conexao("localhost", "root", "", "biblioteca")
df = read_sql(sql.Query_padrao(), con)

#Criar as janelas Iniciais
window1, window2, window3 = gui.Janela_Inicio(), None, None

#Loop de eventos
while True:
    janela,evento,valores = sg.read_all_windows()

    #Quando a janela for fechada
    if janela == window1 and evento == sg.WIN_CLOSED:
        break
    #Quando queremos ir para proxima janela
    if janela == window1 and evento == 'PESQUISAR 🔎':
        window2 = gui.janela_pesquisa()
        window1.hide()

    if janela == window2 and evento == 'Usuários 🧑':
         window3 = gui.pesquisa_usuario()
         window2.hide()

    #Quando queremos voltar para janela anterior

    if janela == window2 and evento == 'Voltar':
        window2.close()
        window1.un_hide()

    if janela == window3 and evento == 'Voltar':
         window3.close()
         window2.un_hide()
         
    #Lógica de eventos dos botões    
    if janela == window1 and evento == 'ADICIONAR ➕': 
            sql.insere_emprestimo(con, str((valores['id-usuario'])),str((valores['id-livro'])),str((valores['data-empr'])),str((valores['data-devol'])))
            df = read_sql(sql.Query_padrao(), con)
            # Atualiza a tabela com os dados do df
            janela['-TABLE-'].update(values=df.values.tolist())

"""         if is_valid_date(valores['data-empr']) == True and extract_date_parts(valores['data-empr']) == True and is_valid_date(valores['data-devol']) == True and (extract_date_parts(valores['data-devol']) != None): """

"""             if (int((valores['id-usuario'])) > (df.shape[0])) or (int((valores['id-usuario'])) < 1) or (isinstance(int((valores['id-usuario'])), int) == False):
                janela['-MSG-'].update('* ID Inválido.')
                for i in range(125):
                    eventos, valores =janela.read(100)
                janela['-MSG-'].update('*mensagem')
            else: """