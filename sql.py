from mysql.connector import cursor, connect
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


    cursor.close()