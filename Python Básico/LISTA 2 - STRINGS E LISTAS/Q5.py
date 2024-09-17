'''5. Ler números inteiros e armazená-los em 2 vetores de tamanho N, com N
informado pelo usuário antes, somar os 2 vetores, imprimir os 2 vetores e depois
o vetor resultado.'''
n = float(input('Digite o tamanho dos vetores: '))
n = int(n)
v1 = []
v2 = []
soma = []

for i in range(n):
    v1.append(float(input('Digite um valor para ser adicionado no vetor 1: ')))
    v2.append(float(input('Digite um valor para ser adicionado no vetor 2: ')))
    soma.append(v1[i]+v2[i])

print(v1)
print(v2)
print(soma)


