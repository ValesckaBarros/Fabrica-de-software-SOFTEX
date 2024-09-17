n = int(input('Qual a quantidade de números que deseja comparar? '))
menor = float(input(f'Digite o número {1}: '))
for i in range(n-1):
    x = float(input(f'Digite o número {i+2}: '))
    if x < menor:
        menor = x
print(f'O menor número é: {menor}')