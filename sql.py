from mysql.connector import cursor, connect

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

def select_todos_usuarios(con):
    cursor = con.cursor()
    sql = "SELECT nome, id  FROM usuarios"
    cursor.execute(sql)

    for (nome, id) in cursor:
        print(nome, id)
    
    cursor.close()