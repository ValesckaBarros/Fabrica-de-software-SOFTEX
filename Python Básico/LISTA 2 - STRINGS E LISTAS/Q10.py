'''10. Altere o programa anterior para garantir que o usuário digitará no máximo 1000
números.'''

lista = []*5
tam = 0
num = int(input('Número: '))
while num<0:
    num = int(input('Número: '))

while num>=0:
    if num>9 and num<100:
        lista.append(num)
        num = int(input('Número: '))
        tam = len(lista)
    else: 
        num = int(input('Número: '))
    if tam>=5:
        num = -1
    

a = len(lista)

for i in range(a-1, -1, -1):
    print(lista[i])
