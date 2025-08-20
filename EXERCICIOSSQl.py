import sqlite3
# CRIE A CONEXÃO
conexao = sqlite3.connect("MEU BANCOS DE DADOS")
# CRIE UM CURSOS PARA PODER EXECUTAR A LINGUAGEM SQL
cursor = conexao.cursor()
#CRIAR UMA TABELA
cursor.execute('''
               create table if not exists pessoas(
               id interger primary key autoincrement not null,
               nome text interger not null,
               cidade text not null
               )
               ''')

# INSERIR DADOS NA TABELA
nome = input("DIGITE SEU NOME")
idade = int(input("DIGITE A SUA IDADE"))
cidade = input ("CIDADE")
cursor.execute('''
               INSERT INTO pessoas (nome.idade,cidade)
               VALUES (?,?,?)
               ''',(nome,idade,cidade))
#CONFIRMAR A TRANSAÇÃO
conexao.commit
# CONSULTOR DADOS DA TABELA
cursor.execute('SELET','FROM PESSOAS')
# MOSTRAR OS DADOS CONSULTADOS
for pessoa in pessoas:
    print(f'''ID: {pessoa},{idade},)

# fechar a conexao
          conexao.close()















