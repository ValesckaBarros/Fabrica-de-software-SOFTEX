#q2
n = int(input('Número: '))
while n>=0:
	n = int(input('digite um numero negativo: '))
lista = []
while n!=0:
	if n<0:
		lista.append(n)
	n = int(input('Número: '))
	while n>0:
		n = int(input('digite um numero negativo: '))
	if len(lista) >= 5: 
		n = 0
	print(lista)
	print(n)

#resultado 1
a = len(lista)
for i in range(a-1, -1, -1):
	if (lista[i]<-9) and (lista[i]>-100) and lista[i]%5==0:
		print(lista[i])

#resultado 2
maior = -99999999999999
for i in lista:
	if i%7 != 0:
		if i>maior:
   			maior = i

print(lista)
print(maior)               









