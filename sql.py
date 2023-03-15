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
