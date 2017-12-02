# cada elemento dos dicionários é formado por chave: valor
# dicionários não garantem ordem

d = {'anderson': 21, 'joao': 30, 'maria': 20}

print(d['anderson'])
print(d['maria'])

print(d.keys())

print(d)
del d['joao']
print(d)

print('anderson' in d)
print('pedro' in d)
print(d.values())