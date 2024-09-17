n = int(input('Digite a quantidade de números que deseja calcular a média: '))
soma = 0
for i in range(n):
    x = float(input(f'Digite o número {i+1}: '))
    soma += x
print(f'A média dos {n} números digitados é: {soma/n}')
