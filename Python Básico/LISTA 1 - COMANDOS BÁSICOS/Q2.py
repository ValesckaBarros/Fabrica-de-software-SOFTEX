n1 = int(input('digite o primeiro número: '))
n2 = int(input('digite o segundo número: '))

while n2 == 0:
    print('Não é possível realizar esta operação! ')
    n2 = int(input('digite o segundo número novamente: '))

resto = n1 % n2

if resto == 0:
    print(n1)
else:
    print(resto**2)