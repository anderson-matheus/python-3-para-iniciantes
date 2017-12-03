'''
Fibonacci
	1, 1, 2, 3, 5, 8, 13
'''

print('\nFibonacci:')
def fib(n):
	if n == 1 or n == 2:
		return 1
	return fib(n - 1) + fib(n - 2)

print(fib(6))


print('\nPotência:')
def pot(b, e):
	r = 1
	for i in range(e+1):
		if i == 0:
			r *= 1
		else:
			r *= b
	
	return r

def pot2(b, e):
	if e == 0:
		return 1
	return b * pot(b, e - 1)

print(pot(2, 10))
print(pot2(2, 10))

print('\nVerifica se um número é par:')
def isPar(n):
	if(n % 2 == 0):
		return True
	return False

print(isPar(2))
print(isPar(3))

print('\nVerifica se um número é primo:')
def isPrimo(n):
	div = 0
	for i in range(1, n+1):
		if(n % i == 0):
			div += 1

	if(div == 2):
		return True

	return False

print(isPrimo(11))