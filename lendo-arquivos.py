arquivo = open('lendo-arquivos.txt', 'r')
print(arquivo.read())
arquivo.close()

with open('lendo-arquivos.txt', 'r') as f:
		print(f.read())
		f.close()