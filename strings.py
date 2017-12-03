'''
strings são imutáveis em python
'''
nome = 'Anderson'
print(nome)

print(nome[0])
print(nome[1])
print(nome[2])
print(nome[6])

lista = list(nome)
print(lista)

lista[0] = 'e'
nome = ''.join(lista)
print(nome)