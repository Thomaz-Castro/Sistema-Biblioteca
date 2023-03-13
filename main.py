import sql


con = sql.criar_conexao("localhost", "root", "", "biblioteca")


sql.insere_usuario(con, "joséfa", "Rua Carvalho", "Bosque dos eucalipitos", "são josé dos campos", "sp", "f", "12932143241", "joséfa@gmail.com")

sql.select_todos_usuarios(con)

sql.fechar_conexao(con)

print('okok')