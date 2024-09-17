'''9. Ler uma seqüência de números inteiros positivos (ou zero). A leitura deve parar
com a digitação de um número negativo. O seu programa deve imprimir os
números lidos cujos valores têm dois dígitos significativos, mas na ordem inversa
em que forem lidos - o último número lido deve ser o primeiro a ser impresso.'''
lista = []
num = int(input('Número: '))
while num<0:
    num = int(input('Número: '))

while num>=0:
    if num>9 and num<100:
        lista.append(num)
    num = int(input('Número: '))

a = len(lista)

for i in range(a-1, -1, -1):
    print(lista[i])


