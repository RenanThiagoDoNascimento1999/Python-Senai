nome = input("DIGITA SEU NOME: ")
chances = 3
while chances > 0:
    senha = input("DIGITAR A SENHA:")

    if senha == '123':
        print('correto')
        break
    else:
        print("INCORRETO")
        chances -= 1
        print("QUAMTIDADE DE CHANCES:", chances)

nota1 = float(input("DIGITA A NOTA DE MATEMATICA:"))
nota2 = float(input("DIGITA A NOTA DE PORTUGUES:"))
nota3 = float(input("DIGITAR A NOTA DE INGLES: "))
media = (nota1+nota2+nota3)/3
print("A MEDIA É:", media)

if media >= 7:
    print("APROVADO")
else:
    print("REPROVADO")

























