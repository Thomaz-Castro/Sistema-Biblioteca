import sql
from random import randrange
from time import sleep

con = sql.criar_conexao("localhost", "root", "", "biblioteca")

""" nomes = ['João Silva', 'Maria Santos', 'Pedro Oliveira', 'Ana Pereira', 'Lucas Souza', 'Carla Fernandes', 'Gustavo Rodrigues', 'Beatriz Almeida', 'Marcos Costa', 'Fernanda Castro', 'Rafael Miranda', 'Mariana Cardoso', 'Thiago Rocha', 'Juliana Santos', 'André Alves', 'Isabela Gomes', 'Felipe Barbosa', 'Gabriela Lima', 'Marcelo Mendes', 'Camila Xavier', 'Leonardo Nascimento', 'Vanessa Barbosa', 'Diego Carvalho', 'Larissa Ribeiro', 'Luiz Eduardo', 'Aline Oliveira', 'Vinícius Cardoso', 'Tatiana Silva', 'Bruno Pereira', 'Sara Oliveira', 'Luana Rodrigues', 'Rodrigo Souza', 'Carolina Silva', 'Renan Costa', 'Luiza Santos', 'Luciano Oliveira', 'Ana Carolina', 'Marcela Almeida', 'Eduardo Fernandes', 'Rita Nunes', 'Fábio Soares', 'Viviane Costa', 'Geraldo Rodrigues', 'Amanda Santos', 'José Almeida', 'Lorena Xavier', 'Arthur Nascimento', 'Cristina Santos', 'Roger Carimba', 'Gisele Gonçalves']

sexos = ['m', 'f', 'm', 'f', 'm', 'f', 'm', 'f', 'm', 'f', 'm', 'f', 'm', 'f', 'm', 'f', 'm', 'f', 'f', 'f', 'm', 'f', 'm', 'f', 'm', 'f', 'm', 'f', 'm', 'f', 'f', 'm', 'f', 'm', 'f', 'm', 'f', 'f', 'm', 'f', 'm', 'f', 'm', 'f', 'm', 'f', 'm', 'f', 'm', 'f']

cidades = ['Santópolis  do Aguapeí', 'São José dos Campos', 'Recife', 'São José dos Campos', 'Campinas', 'São José dos Campos', 'São José dos Campos', 'São José dos Campos', 'São José dos Campos', 'São José dos Campos', 'Rio de Janeiro', 'São José dos Campos', 'Belo Horizonte', 'Curitiba', 'São José dos Campos', 'São José dos Campos', 'São José dos Campos', 'Porto Alegre', 'São José dos Campos', 'São José dos Campos', 'Salvador', 'São José dos Campos', 'São José dos Campos', 'São José dos Campos', 'Uberlândia', 'São José dos Campos', 'São José dos Campos', 'São José dos Campos', 'São José dos Campos', 'Blumenau', 'São Paulo', 'Cuiabá', 'São José dos Campos', 'São José dos Campos', 'Fortaleza', 'São José dos Campos', 'São José dos Campos', 'São José dos Campos', 'São José dos Campos', 'São José dos Campos', 'São José dos Campos', 'São José dos Campos', 'São José dos Campos', 'São José dos Campos', 'São José dos Campos', 'São José dos Campos', 'São José dos Campos', 'São José dos Campos', 'São José dos Campos', 'São José dos Campos']

estados = ['SP', 'SP', 'PE', 'SP', 'SP', 'SP', 'SP', 'SP', 'SP', 'SP', 'RJ', 'SP', 'MG', 'PR', 'SP', 'SP','SP', 'RS', 'SP', 'SP', 'BA', 'SP', 'SP', 'SP', 'MG', 'SP', 'SP', 'SP', 'SP', 'SC', 'SP', 'MT','SP', 'SP', 'CE', 'SP', 'SP', 'SP', 'SP', 'SP', 'SP', 'SP', 'SP', 'SP', 'SP', 'SP', 'SP', 'SP', 'SP', 'SP']


bairros = ['Centro', 'Jardim', 'Vila', 'Bela Vista', 'Jardim das Flores', 'Jardim Europa', 'Jardim América', 'Jardim Paulista', 'Alphaville', 'Morumbi', 'Pinheiros', 'Moema', 'Santana', 'Tatuapé', 'Vila Mariana', 'Liberdade', 'Campo Belo', 'Cambuí', 'Cidade Jardim', 'Brooklin', 'Paraíso', 'Perdizes', 'Itaim Bibi', 'Vila Olímpia', 'Jardins','Centro', 'Jardim', 'Vila', 'Bela Vista', 'Jardim das Flores', 'Jardim Europa', 'Jardim América', 'Jardim Paulista', 'Jardim São Paulo', 'Alphaville', 'Morumbi', 'Pinheiros', 'Moema', 'Santana', 'Tatuapé', 'Vila Mariana', 'Campo Belo', 'Cambuí', 'Cidade Jardim', 'Brooklin', 'Paraíso', 'Perdizes', 'Itaim Bibi', 'Vila Olímpia', 'Jardins']

enderecos =['Rua dos Eucaliptos, 214', 'Rua São Paulo, 452', 'Rua dos Ipês, 906', 'Rua das Margaridas, 309', 'Avenida das Acácias, 53', 'Rua dos Cravos, 824', 'Rua das Azaléias, 189', 'Avenida das Rosas, 697', 'Rua das Orquídeas, 422', 'Avenida dos Lírios, 56', 'Rua dos Girassóis, 701', 'Avenida dos Jardins, 230', 'Rua das Violetas, 469', 'Rua das Tulipas, 814', 'Avenida dos Pinheiros, 925', 'Rua das Palmeiras, 102', 'Rua das Magnólias, 286', 'Avenida das Hortênsias, 559', 'Rua das Flores, 183', 'Avenida dos Cactos, 677', 'Rua das Bromélias, 328', 'Avenida das Begônias, 778', 'Rua dos Jasmins, 121','Avenida das Margaridas, 453', 'Rua dos Narcisos, 989', 'Rua das Camélias, 502','Rua dos Eucaliptos, 214', 'Avenida Brasil, 703', 'Rua São Paulo, 452', 'Rua dos Ipês, 906', 'Rua das Margaridas, 309', 'Avenida das Acácias, 53', 'Rua dos Cravos, 824', 'Rua das Azaléias, 189', 'Avenida das Rosas, 697', 'Rua das Orquídeas, 422', 'Avenida dos Lírios, 56', 'Avenida dos Jardins, 230', 'Rua das Tulipas, 814', 'Avenida dos Pinheiros, 925', 'Rua das Palmeiras, 102', 'Rua das Magnólias, 286', 'Avenida das Hortênsias, 559', 'Rua das Flores, 183', 'Avenida dos Cactos, 677', 'Rua das Bromélias, 328', 'Avenida das Begônias, 778', 'Rua dos Jasmins, 121', 'Rua dos Narcisos, 989', 'Rua das Camélias, 502']

emails = ['JoãoSilva@gmail.com', 'MariaSantos@gmail.com', 'PedroOliveira@gmail.com', 'AnaPereira@gmail.com', 'LucasSouza@gmail.com', 'CarlaFernandes@gmail.com', 'GustavoRodrigues@gmail.com', 'BeatrizAlmeida@gmail.com', 'MarcosCosta@gmail.com', 'FernandaCastro@gmail.com', 'RafaelMiranda@gmail.com', 'MarianaCardoso@gmail.com', 'ThiagoRocha@gmail.com', 'JulianaSantos@gmail.com', 'AndréAlves@gmail.com', 'IsabelaGomes@gmail.com', 'FelipeBarbosa@gmail.com', 'GabrielaLima@gmail.com', 'MarceloMendes@gmail.com', 'CamilaXavier@gmail.com', 'LeonardoNascimento@gmail.com', 'VanessaBarbosa@gmail.com', 'DiegoCarvalho@gmail.com', 'LarissaRibeiro@gmail.com', 'LuizEduardo@gmail.com', 'AlineOliveira@gmail.com', 'ViníciusCardoso@gmail.com', 'TatianaSilva@gmail.com', 'BrunoPereira@gmail.com', 'SaraOliveira@gmail.com', 'LuanaRodrigues@gmail.com', 'RodrigoSouza@gmail.com', 'CarolinaSilva@gmail.com', 'RenanCosta@gmail.com', 'LuizaSantos@gmail.com', 'LucianoOliveira@gmail.com', 'AnaCarolina@gmail.com', 'MarcelaAlmeida@gmail.com', 'EduardoFernandes@gmail.com', 'RitaNunes@gmail.com', 'FábioSoares@gmail.com', 'VivianeCosta@gmail.com', 'GeraldoRodrigues@gmail.com', 'AmandaSantos@gmail.com', 'JoséAlmeida@gmail.com', 'LorenaXavier@gmail.com', 'ArthurNascimento@gmail.com', 'CristinaSantos@gmail.com', 'RogerCarimba@gmail.com', 'GiseleGonçalves@gmail.com']

telefones = ['5128437260', '8992783924', '5394387250', '7994185323', '2597209810', '2376914120', '6929660303', '3328169816', '2095294009', '2890957433', '8325610321', '9177991352', '9921332612', '2600752182', '3903038531', '0585859930', '3381012425', '3250621363', '4085764355', '0486324877', '5832764351', '6103591271', '6939331401', '0150823614', '2650757185', '0106114729', '1440413252', '5838518299', '0271160870', '3135911140', '2915085665', '9157424742', '4507280954', '6633965459', '9326020015', '8363932700', '5972546573', '3185942920', '5279396193', '5707892702', '8000197016', '9678649333', '1652912375', '2125103972', '0673274734', '8165306713', '6124986274', '3998065039', '6866755926', '7065496948']

for i in range (0, 50):
    nome = str(nomes[i])
    endereco = str(enderecos[i])
    bairro = str(bairros[i])
    cidade = str(cidades[i])
    estado = str(estados[i])
    sexo = str(sexos[i])
    telefone = str(telefones[i])
    email = str(emails[i])
    sql.insere_usuario(con, nome, endereco, bairro, cidade, estado, sexo, telefone, email)
    print('{} - {} ADICIONADO'.format(i, nome))
    sleep(0.5)

print('\nOs 50 foram adicionados') """

""" editoras = ['Livrosaurus', 'Aquarela Editorial', 'Ática Livros', 'Verus Editora', 'Leitura',
            'Livraria Cultura', 'Companhia das Letras', 'Record', 'Suma de Letras', 'Globo Livros',
            'Intrínseca', 'Saraiva', 'Novo Século', 'L&PM Editores', 'Editora Rocco']


for i in range(0, 15):
    nome = str(editoras[i])
    sql.insere_editora(con, nome)
    print('{} - {} ADICIONADO'.format(i, nome))
    sleep(0.5)

print('\nOs 15 foram adicionados')  """

""" autores = ['Isaac Freitas', 'Marina Santos', 'Felipe Cardoso', 'Amanda Costa', 'Gabriel Souza',
            'Carla Pereira', 'Thiago Ferreira', 'Ana Paula Silva', 'João Carvalho', 'Mariana Oliveira',
            'Leonardo Martins', 'Fernanda Ramos', 'Roberto Almeida', 'Rafaela Santos', 'Lucas Alves',
            'Camila Rodrigues', 'Renato Silva', 'Bianca Vieira', 'Bruno Gomes', 'Julia Castro', 'Jefersson Andrade'
            'Luciana Barbosa', 'Diego Moraes', 'Vivian Miranda', 'Rodrigo Costa', 'Alessandra Gonçalves',
            'Ricardo Oliveira', 'Giovanna Santos', 'Lucas Almeida', 'Mariana Fernandes', 'André Moreira',
            'Lívia Rodrigues', 'Guilherme Silva', 'Cristiane Martins', 'Pedro Souza', 'Elisa Oliveira', 'Ricardo Eliseus', 'Gabriela Costa', 'Victor Santos', 'Luiza Lima']

sexos = ['m','f','m','f','m','f','m','f','m','f','m','f','m','f','m','f','m','f','m','f''m','f','m','f','m','f','m','f','m','f','m','f','m','f','m','f','m','f','m','f'
]

for i in range(0, 39):
    nome = str(autores[i])
    sexo = str(sexos[i])
    sql.insere_autor(con, nome, sexo)
    print('{} - {} ADICIONADO'.format(i, nome))
    sleep(0.5)

print('\nOs 39 foram adicionados')  """

titulos = ['O Destino do Universo', 'A Última Chance', 'A Trilha da Montanha', 'O Amor Proibido',
          'As Sombras do Passado', 'O Mistério do Bosque', 'O Colecionador de Almas', 'A Busca Pela Verdade',
          'O Jogo da Vingança', 'O Segredo da Ilha', 'A Estrela Solitária', 'A Cor do Sangue',
          'O Último Suspiro', 'A Queda do Império', 'A Jornada do Herói', 'A Dança da Morte',
          'A Promessa do Amanhã', 'A Fuga do Labirinto', 'A Porta do Conhecimento', 'O Espelho da Alma',
          'A Chave do Mistério', 'O Guardião do Tesouro', 'O Reino do Silêncio', 'A Luz do Entardecer',
          'A Face do Mal', 'O Despertar da Magia', 'A Noite das Bruxas', 'A Última Resistência', 'O Poder do Infinito',
          'O Lado Sombrio da Lua', 'A Caça ao Tesouro', 'O Mestre da Ilusão', 'A Queda do Céu', 'A Maldição da Lua Cheia',
          'O Segredo do Abismo', 'A Busca Pela Cura', 'O Labirinto da Memória', 'A Fonte da Eternidade', 'O Refúgio dos Anjos',
          'A Cidade dos Segredos', 'O Poder da Alma', 'A Vingança do Destino', 'O Último Herdeiro', 'A Marca do Passado',
          'O Lado Oculto da Realidade', 'A Conspiração dos Poderosos', 'A Sombra da Inocência', 'A Queda do Dragão',
          'O Enigma da Pirâmide', 'O Portal da Magia', 'O Mistério do Antigo Manuscrito', 'O Último Refúgio',
          'A Lenda do Guerreiro', 'A Voz da Consciência', 'O Reino das Trevas', 'A Marca do Mal', 'A Espada da Justiça',
          'O Legado do Passado', 'A Trama do Destino', 'O Guardião da Verdade', 'A Cidade dos Anjos',
          'A Cruzada dos Heróis', 'O Espectro da Vingança', 'A Chama da Revolta', 'O Mistério do Relógio',
          'O Poder do Amor', 'A Queda do Império Romano', 'A Sombra da Morte', 'A Busca pela Redenção', 'O Silêncio da Floresta',
          'O Segredo do Sótão', 'A Cidade das Sombras', 'O Mistério do Espelho',
          'A Queda do Reino', 'O Labirinto da Solidão', 'A Fonte da Juventude', 'O Refúgio das Fadas', 'O Reino Perdido',
          'A Cidade dos Mistérios', 'O Poder da Magia Negra', 'A Vingança do Assassino', 'A Marca da Traição', 'A Sombra do Demônio',
          'A Queda dos Gigantes', 'O Enigma da Esfinge', 'A Ilha do Tesouro', 'A Jornada do Viajante', 'O Tesouro do Pirata',
          'A Queda do Império Inca', 'O Poder da Vingança', 'O Mistério do Castelo', 'A Promessa do Amor', 'O Lado Escuro da Verdade',
          'A Última Noite', 'O Dom da Vida', 'A Cidade dos Anjos Caídos', 'A Luz da Esperança', 'A Marca da Escuridão',
          'O Último Capítulo', 'A Queda do Poderoso', 'O Segredo da Caverna', 'A Jornada da Alma', 'O Refúgio da Natureza',
          'A Chama da Liberdade', 'O Retorno do Herói', 'A Face do Perigo', 'O Enigma do Labirinto', 'A Queda da Dinastia',
          'A Noite do Terror', 'O Poder da Coragem', 'A Trama da Conspiração', 'A Maldição do Sangue', 'A Luz da Vitória',
          'A Queda do Império Otomano', 'A Sombra do Passado', 'O Legado do Mistério', 'A Cidade do Futuro', 'O Colecionador de Sonhos',
          'A Busca Pelo Poder', 'O Fim do Mundo', 'A Espada da Vingança', 'O Retorno da Magia', 'A Face do Medo',
          'O Último Desafio', 'A Queda do Herói', 'O Mistério do Oceano', 'A Marca do Tempo', 'A Jornada do Guerreiro',
          'A Sombra do Dragão', 'O Segredo da Floresta', 'A Cidade dos Mundos Paralelos', 'A Busca Pela Sobrevivência', 'O Labirinto da Verdade',
          'A Queda da Monarquia', 'A Noite das Estrelas', 'O Poder da Ilusão', 'A Luz da Solidariedade', 'A Marca do Destino',
          'A Queda da Nação', 'O Labirinto da Obsessão', 'A Trama da Mentira', 'O Segredo do Vale', 'A Jornada do Amor',
          'A Cidade dos Mil Segredos', 'O Poder do Conhecimento', 'A Face da Vingança', 'A Busca Pela Redenção', 'A Luz da Verdade',
          'A Queda do Império Chinês', 'A Sombra do Amor', 'O Legado do Guerreiro', 'A Cidade dos Deuses', 'A Marca da Guerra',
          'O Segredo do Palácio', 'A Queda do Mundo Antigo', 'A Jornada da Cura', 'O Refúgio do Mistério']

isbns = [
    "9780321856715",
    "9780321879721",
    "9780321903046",
    "9780321928421",
    "9780321947736",
    "9780321965518",
    "9780321973667",
    "9780321992781",
    "9780321999162",
    "9780322016579",
    "9780322022280",
    "9780322034597",
    "9780322053536",
    "9780322062392",
    "9780322069179",
    "9780322070632",
    "9780322082147",
    "9780322092900",
    "9780322099312",
    "9780322101848",
    "9780322110581",
    "9780322127428",
    "9780322145835",
    "9780322152727",
    "9780322155568",
    "9780322159580",
    "9780322162320",
    "9780322173326",
    "9780322182274",
    "9780322188863",
    "9780322192785",
    "9780322207441",
    "9780322210595",
    "9780322217624",
    "9780322221621",
    "9780322225087",
    "9780322232962",
    "9780322237257",
    "9780322239268",
    "9780322242732",
    "9780322246891",
    "9780322254131",
    "9780322256401",
    "9780322259556",
    "9780322261993",
    "9780322265427",
    "9780322269272",
    "9780322271886",
    "9780322275211",
    "9780322279325",
    "9780322280543",
    "9780322282868",
    "9780322286996",
    "9780322289959",
    "9780322291649",
    "9780322293308",
    "9780322295104",
    "9780322298426",
    "9780322299362",
    "9780322300563",
    "9780322302802",
    "9780322306213",
    "9780322311071",
    "9780322312900",
    "9780322316793",
    "9780322322565",
    "9780322325443",
    "9780322329281",
    "9780322333707",
    "9780322337811",
    "9780322343478",
    "9780322348084",
    "9780322353453",
    "9780322360772",
    "9780322365074",
    "9780322368709",
    "9780322373499",
    "9780322376490",
    "9780322380602",
    "9780322384860",
    "9780322390960",
    "9780322396054",
    "9780322400133",
    "9780322401253",
    "9780322406470",
    "9780322412120",
    "9780322416623",
    "9780322419822",
    "9780322422945",
    "9780322426714",
    "9780322428619",
    "9780322431879",
    "9780322435464",
    "9780322438809",
    "9780322443292",
    "9780322448952",
    "9780322454649",
    "9780322461531",
    "9780322465195",
    "9780322472100",
    "9780322475217",
    "9780322478898",
    "9780322481270",
    "9780322484707",
    "9780322488903",
    "9780322492078",
    "9780322497776",
    "9780322501480",
    "9780322505051",
    "9780322508793",
    "9780322511526",
    "9780322514343",
    "9780322520054",
    "9780322524915",
    "9780322528623",
    "9780322532613",
    "9780322536789",
    "9780322540519",
    "9780322543268",
    "9780322548768",
    "9780322553755",
    "9780322556879",
    "9780322560951",
    "9780322565154",
    "9780322569381",
    "9780322573020",
    "9780322577448",
    "9780322581056",
    "9780322584521",
    "9780322587898",
    "9780322592014",
    "9780322594681",
    "9780322598009",
    "9780322603079",
    "9780322608173",
    "9780322612958",
    "9780322616871",
    "9780322620916",
    "9780322624648",
    "9780322630458",
    "9780322633466",
    "9780322637426",
    "9780322642017",
    "9780322646145",
    "9780322649337",
    "9780322652696",
    "9780322658032",
    "9780322662978",
    "9780322666624",
    "9780322670386",
    "9780322675060",
    "9780322681016",
    "9780322684086",
    "9780322688602",
    "9780322693309",
    "9780322697840",
    "9780322700145"
]

anos = ['2004', '2022', '2009', '1995', '1994', '1990', '2004', '2012', '1991', '1993', '2008', '2017', '2018', '2005', '1995', '2017', '2021', '2015', '2003', 
'1999', '2002', '2002', '1996', '2018', '2000', '2018', '2018', '1992', '1994', '2011', '2007', '2012', '1998', '1999', '2021', '2019', '1994', '2009', '1996', '2011', '1995', '2022', '2003', '1992', '1994', '1991', '2000', '2002', '1995', '2016', '2004', '2007', '2022', '2000', '1996', '2011', '1998', '2013', '1993', '2012', '2005', '1999', '2009', '2014', '2003', '2011', '2006', '2017', '2021', '2006', '2015', '1999', '2013', '2008', '1990', '2003', '2019', '2007', '2020', '2012', '1998', '1993', '1994', '2008', '1999', '2013', '2018', '2016', '2000', '2019', '2014', '1997', '1992', '1996', '2013', '1998', '2021', '2006', '2017', '1999', '1999', '2008', '2010', '1996', '2022', '1996', '2016', '1991', '2010', '1999', '1991', '2013', '2006', '2019', '1994', '2009', '2004', '2009', '1995', '2019', '2007', '2014', '1993', '2010', '2000', '2002', '1993', '1999', '2002', '2014', '1994', '2015', '2008', '1995', '1991', '2014', '2006', '1994', '2000', '2012', '2009', '2018', '1998', '1995', '2000', '2012', '1991', '2008', '2013', '1994', '2012', '1997', '2017', '1990', '2017', '2008', '2004']

# autores 39
# editoras 15

for i in range(0,157):
    titulo = str(titulos[i])
    autor_id = randrange(1,39)
    autor_id = str(autor_id)
    editora_id = randrange(1, 15)
    editora_id = str(editora_id)
    ano = str(anos[i])
    isbn = str(isbns[i])
    sql.insere_livro(con, titulo, autor_id, editora_id, ano, isbn)
    print('{} - {} ADICIONADO'.format(i, titulo))
    sleep(0.5)

print('\nOs 157 foram adicionados')
