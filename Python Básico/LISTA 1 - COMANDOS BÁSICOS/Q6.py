n = int(input('Digite um número: '))
while n<=0:
    n = int(input('Digite outro número: '))
fatorial = 1
for i in range(1,n+1):
    fatorial = fatorial*i
print(fatorial)

n = int(input('Digite um número: '))
while n<=0: n = int(input('Digite outro número: '))
c=1
fatorial = c
while c<=n:
    fatorial = fatorial*c
    c +=1
print(fatorial)
