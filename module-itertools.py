lista = [1, 2, 3]

from itertools import permutations, combinations

print('\nPermutações\n')
for p in permutations(lista):
	print(p)

print('\nCombinações\n')
for c in combinations(lista, 2):
	print(c)