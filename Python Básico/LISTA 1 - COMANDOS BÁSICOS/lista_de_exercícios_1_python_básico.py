# -*- coding: utf-8 -*-
"""Lista de exercícios 1 - Python Básico.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rRrI_KjrRk4FvLViXGg4XbQw8jQUaAqO

# Q1
"""


"""# Q2"""



"""# Q3"""



"""# Q4"""



"""#Q5"""


"""Q6"""

# RESOLUÇÃO COM FOR
x = int(input('Digite um número: '))
while x<=0: n = int(input('Digite outro número: '))

#a - S = 1 + 3/2 + 4/5 + 6/7...
n = 3
d = 2
s = 1
if x==1:
    s=1
else:
    for i in range(1,x):
        div = n/d
        s = s + div
        n += 1
        d += 1

print(f'resultado = {s}')

# RESOLUÇÃO COM FOR
x = int(input('Digite um número: '))
while x<=0: n = int(input('Digite outro número: '))
#b - S = 2/500 + 5/490 + 2/480 -5/470...= -0,0126 / 4 termos
d = 500
s = 0
for i in range(1,x+1):
    if d>0:
        if i%2 != 0:
            div = 2/d
        else:
            div = -5/d
            s += div
            d -=10
print(f'resultado = {s}')
print(f'qtd termos: {i-1}')

# RESOLUÇÃO COM FOR
x = int(input('Digite um número: '))
while x<=0: n = int(input('Digite outro número: '))
#c - S = 37*38/1 + 36*37/2 + 38*38/3 + 39*40/470...
n = 37
s = 0
for i in range (1, x+1):
    div = (n*(n+1))/i
    print(f'termo: {i} => {n}*{n+1}/{i} = {div}')
    n -= 1
    s += div

print(f'resultado = {s}')

"""#Q7"""

# RESOLUÇÃO COM FOR
x = int(input('Digite um número: '))
y = int(input('Digite outro número: '))

soma=0
if x>y:
    x,y=y,x

for i in range (x,y+1):
    if i%2 != 0:
        soma += i
print(soma)

"""#Q8"""

x = int(input('Digite um número: '))
y = int(input('Digite outro número: '))
print('|{:^10}|{:^10}|'.format('°F', '°C'))
for i in range(x,y+1):
    c = (i-32)*5/9
    print('|{:^10}|{:^10.2}|'.format(i, c))

"""Q9"""

# -1, 0, 5, 6, 11, 12, 17, 18...
x = int(input('Digite um número: '))
n = 0
if x == 1:
    print(-1)
else:
    for i in range(0, x-1):
        print(i)