ecommerce = {
    'LIVROS' : {
        'v1':9.99,
        'v2':7.50,
        'v3':4.50
    },
    'TABLETS' : {
        'V1' :999.99,
        'V2' :500.0,
        'V3' :100.900
    },
    'FONE' : {
        'V1':10.0,
        'V2':20.0,
        'V3':30.0
    }
}

produto1 = float (input("DIGITE O LIVRO  :"))
produto2 = float (input("DIGITE O TABLETS  :")) 
produto3 = float (input("DIGITE O FONE  :"))



soma = sum([produto1,produto2,produto3])
print(f"R$,{soma}")



















