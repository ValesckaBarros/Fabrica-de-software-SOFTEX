def fatorial(n):
	f = 1
	for i in range(1, n+1):
		f = f*i
	return f
		
def serie(n):
	s = 0
	numerador1 = 3
	numerador2 = 5
	
	for i in range(1, n+1):
		if i%2 != 0:
			termo = numerador1/fatorial(i)
			numerador1  = numerador1*5
		else:
			termo = -(numerador2/fatorial(i))
			numerador2 = numerador2*6
		s = s + termo
	return s

#PROGRAMA PRINCIPAL
n = int(input('Número: '))
while n<=0:
	n = int(input('Número: '))

while n>=1:
	print(f'resuldado = {serie(n)}')
	n = int(input('Número: '))