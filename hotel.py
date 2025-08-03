#HOTEL

quartos = {

    'simples': 100,
    'normal': 500,
    'luxo' : 10000,
}

Escolha_quartos = input("ESCOLHA SEU QUARTO:")

if Escolha_quartos == 'simples':
    print("O PREÇO DO QUARTO R$: ", quartos['simples'])
    dias = int (input("Quantos dias vai ficar:"))
    total = dias * quartos['simples']
    print('total: R$',total)
    
elif Escolha_quartos == 'normal':
    print("O PREÇO DO QUARTO R$: ",quartos['normal'])
    dias = int (input("Quantos dias vai ficar:"))
    total = dias * quartos['normal']
    print('total: R$',total)
    
elif Escolha_quartos == 'luxo':
    print("O PREÇO DO QUARTO R$: ", quartos['luxo'])
    dias = int (input("Quantos dias vai ficar:"))
    total = dias * quartos['luxo']
    print('total: R$',total)
else:
    print("QUARTO NÃO ENCONTRADO")


nome = input("DIGITA SEU NOME:")
idade = input("DIGITA A SUA IDADE:")
cpf = input("DIGITA SEU CPF:")
senha = input("DIGITA SUA SENHA:")

if len (cpf) == 8:
    print("CORRETO")
else:
    print("INCORRETO")
if len (senha) == 6:
    print("CORRETO")
else:
    print("INCORRETO")        
    


























