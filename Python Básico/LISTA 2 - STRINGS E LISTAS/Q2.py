'''2. Ler o nome do usuário e imprimi-lo em formato de escala, ou seja, só a primeira
letra na primeira linha, as duas primeiras letras na segunda linha, e assim por
diante.'''

nome  = input('Digite o seu nome: ')

c = 1
while c<=len(nome):
    for i in range(c):
        print(nome[i], end=" ")
        
    print('')
    c +=1
