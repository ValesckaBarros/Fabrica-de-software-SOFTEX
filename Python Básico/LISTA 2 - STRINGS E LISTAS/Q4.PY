'''4. Ler o nome completo do usuário e imprimi-lo com o primeiro e último nome
escritos todo em maiúsculas.'''

nome = input('Digite seu nome completo: ')

a = nome.split()

print(a)

nome1 = a[0].upper()
for i in range(1, len(a)-1):
    nome1 += (" " + a[i]) 
nome1 += (" " + a[len(a)-1].upper())

print(nome1)





