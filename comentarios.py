# comentário em linha

'''
comentário
em várias
linhas
'''

"""
outra forma
de comentar em
várias linhas
"""

# 1, 1, 2, 3, 5, 8, 13...
def fib(n):
	if n == 1 or n == 2:
		return 1

	return fib(n -1) + fib(n - 2)

print(fib(6))