from mysql.connector import connect
import pandas as pd

def criar_conexao(host, usuario, senha, banco):
    return connect(host=host, user=usuario, password=senha, database=banco)
def fechar_conexao(con):
    return con.close()


def insere_usuario(con, nome, endereco, bairro, cidade, estado, sexo, telefone, email):
    cursor = con.cursor()
    code = "INSERT INTO usuarios values (default, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(nome, endereco, bairro, cidade, estado, sexo, telefone, email)
    cursor.execute(code)
    cursor.close()
    con.commit()
def delete_usario(con, id):
    cursor = con.cursor()
    code = "Delete from usuarios where id = '{}'".format(id)
    cursor.execute(code)
    cursor.close()
    con.commit()
def select_todos_usuarios(con):
    query = "SELECT * FROM usuarios"
    df = pd.read_sql(query, con)
    return df


def insere_editora(con, nome):
    cursor = con.cursor()
    code = "INSERT INTO editoras values (default, '{}')".format(nome)
    cursor.execute(code)
    cursor.close()
    con.commit()
def delete_editora(con, id):
    cursor = con.cursor()
    code = "Delete from editoras where id = '{}'".format(id)
    cursor.execute(code)
    cursor.close()
    con.commit()
def select_todos_editoras(con):
    query = "SELECT * FROM editoras"
    df = pd.read_sql(query, con)
    return df


def insere_autor(con, nome, sexo):
    cursor = con.cursor()
    code = "INSERT INTO autores values (default, '{}', '{}')".format(nome,sexo)
    cursor.execute(code)
    cursor.close()
    con.commit()
def delete_autor(con, id):
    cursor = con.cursor()
    code = "Delete from autores where id = '{}'".format(id)
    cursor.execute(code)
    cursor.close()
    con.commit()
def select_todos_autores(con):
    query = "SELECT * FROM autores"
    df = pd.read_sql(query, con)
    return df


def insere_livro(con, titulo, autor_id, editora_id, ano_publicacao, isbn):
    cursor = con.cursor()
    code = "INSERT INTO livros values (default, '{}', '{}', '{}', '{}', '{}')".format(titulo, autor_id, editora_id, ano_publicacao, isbn)
    cursor.execute(code)
    cursor.close()
    con.commit()
def delete_livro(con, id):
    cursor = con.cursor()
    code = "Delete from livros where id = '{}'".format(id)
    cursor.execute(code)
    cursor.close()
    con.commit()
def select_todos_livros(con):
    query = "SELECT * FROM livros"
    df = pd.read_sql(query, con)
    return df

def insere_emprestimo(con, usuario_id, livro_id, data_emprestimo, data_devolucao):
    cursor = con.cursor()
    code = "INSERT INTO emprestimos values (default, '{}', '{}', '{}', '{}')".format(usuario_id, livro_id, data_emprestimo, data_devolucao)
    cursor.execute(code)
    cursor.close()
    con.commit()
def delete_emprestimo(con, id):
    cursor = con.cursor()
    code = "Delete from emprestimos where id = '{}'".format(id)
    cursor.execute(code)
    cursor.close()
    con.commit()
def select_todos_emprestimos(con):
    query = "SELECT * FROM emprestimos"
    df = pd.read_sql(query, con)
    return df


def Query_padrao():
    query = """select u.nome, l.titulo, aut.nome, edit.nome,l.isbn , empr.data_emprestimo, empr.data_devolucao  from emprestimos as empr join usuarios as u on u.id = empr.usuario_id join livros as l on l.id = empr.livro_id join autores as aut on aut.id = l.autor_id join editoras as edit on edit.id = l.editora_id order by empr.id desc;"""
    return query