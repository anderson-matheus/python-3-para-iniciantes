# conjuntos não permiter elementos repetidos e eles não são ordenados

c = {2, 2, 2, 2, 'marcos', 'marcos'}
print(c)
print(len(c))

lista = [1, 1, 1, 2, 2, 2, 3, 3]
c = set(lista)
print(c)

c.add(2)
print(c)

c.add('anderson')
print(c)
print(type(c))

c.remove('anderson')
print(c)