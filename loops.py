c = 0


import time
while c <= 10:     # condição
    print(c)
    c = c  +  1
    time.sleep(2)

lista = [[1,2,3],[4,5,6]]


for n in lista:
    for x  in n:
        pass
        print(x)
    print(n) 


dicionario = {
'key 1' : 'Value 1',
'key 2' : 'Value 2' 
}


l_chaves = []
l_valores = []


for l_chave in dicionario.items():
    l_chaves.append(l_chave)
    # l_valores.append(l_valore)


print(l_valores)
print(l_chaves)  



































