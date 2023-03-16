import sql


con = sql.criar_conexao("localhost", "root", "", "biblioteca")

print('\033[1;35m')
print(r"""
------------------------------------------------------------------------------------------------------------------------
 ______   _______  _        _______  _______        ______   _______        ______   _______  ______   _______  _______ 
(  ___ \ (  ___  )( (    /|(  ____ \(  ___  )      (  __  \ (  ____ \      (  __  \ (  ___  )(  __  \ (  ___  )(  ____ \
| (   ) )| (   ) ||  \  ( || (    \/| (   ) |      | (  \  )| (    \/      | (  \  )| (   ) || (  \  )| (   ) || (    \/
| (__/ / | (___) ||   \ | || |      | |   | |      | |   ) || (__          | |   ) || (___) || |   ) || |   | || (_____ 
|  __ (  |  ___  || (\ \) || |      | |   | |      | |   | ||  __)         | |   | ||  ___  || |   | || |   | |(_____  )
| (  \ \ | (   ) || | \   || |      | |   | |      | |   ) || (            | |   ) || (   ) || |   ) || |   | |      ) |
| )___) )| )   ( || )  \  || (____/\| (___) |      | (__/  )| (____/\      | (__/  )| )   ( || (__/  )| (___) |/\____) |
|/ \___/ |/     \||/    )_)(_______/(_______)      (______/ (_______/      (______/ |/     \|(______/ (_______)\_______)
------------------------------------------------------------------------------------------------------------------------                                                                                                                     """)
print('\033[m')

print('='*30)

choice = int(input("Que atividade voce quer realizar? \n[1]- Inserir usuário\n[2]- Deletar usuário\n[3]- Ver usuários\nEscolha: "))

print('')

if choice == 1:
    nome = input("Digite o nome do usuário: ")
    endereco = input("Digite o endereço do usuário: ")
    bairro = input("Digite o bairro do usuário: ")
    cidade = input("Digite a cidade do usuário: ")
    estado = input("Digite o estado do usuário: ")
    sexo = input("Digite o sexo do usuário: ")
    telefone = input("Digite o telefone do usuário: ")
    email = input("Digite o email do usuário: ")

    sql.insere_usuario(con, nome, endereco, bairro, cidade, estado, sexo, telefone, email)

elif choice == 2:
    aidi = str(input("Digite o id do usuário a ser deletado: "))
    sql.delete_usario(con,aidi)

elif choice == 3:
    print(sql.select_todos_usuarios(con))

sql.fechar_conexao(con)

print('\nokok')