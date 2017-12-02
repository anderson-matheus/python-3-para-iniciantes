# listas podem ser heterogêneas
lista = [1, 2, 3, 4]
print(lista)

lista = [1, 2, 'anderson', 'matheus', 3.14, 8,76]
print(lista)
print(lista[0])
print(lista[2])

lista = [1, 'marcos', 3.14]
print(lista)

lista.append('joao')
print(lista)
print(lista[-1])
print(len(lista))

lista2 = [2, 3, 4]
lista.extend(lista2)
print(lista)

lista.insert(0, 'maria')
print(lista)

lista.insert(2, 'yankee')
print(lista)

lista = [1, 2, 3, 4]
print(lista)

lista.remove(3)
print(lista)

lista = [1, 'anderson', 3.14]
print(lista)

lista.remove('anderson')
print(lista)

lista.pop(1)
print(lista)

lista = ['anderson', 'python', 10]
print(lista)

lista.clear()
print(lista)

lista = ['anderson', 'python', 10]
print(lista)
print(lista.index('python'))

lista = ['python', 'python', 'php']
print(lista.count('python'))

lista = [10, 5, 3, 7]
print(lista)

lista.sort()
print(lista)

