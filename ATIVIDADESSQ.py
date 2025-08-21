import sqlite3

conn = sqlite3.connect('AGENCIA_DE_MARKETING.db')

cursor = conn.cursor()
# CRIANDO A TABELA SEMPRE NÃO BOTA A VIRGULA NA ULTIMA LINHA 
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    idade INTEGER,
    email TEXT NOT NULL,
    endereço TEXT NOT NULL,
    trabalho TEXT NOT NULL,
    graduação TEXT NOT NULL         
)
''')

nome =  input('NOMES: ')
idade =  int(input('IDADE: '))
cidade = input('CIDADE: ')
email = input ('E-MAIL:')
endereço = input('ENDEREÇO:')
trabalho = input('TRABALHO:')
graduação = input('GRADUAÇÃO:')

#INSERIR OS CODIGOS 
cursor.execute('''INSERT INTO clientes(nome, idade, cidade,email,endereço,trabalho,graduação)
          values (?,?,?,?,?,?,?)''',(nome, idade, cidade,email,endereço,trabalho,graduação))

conn.commit()
conn.close()

print('CLIENTE CADASTRADO COM SUCESSO')































































































