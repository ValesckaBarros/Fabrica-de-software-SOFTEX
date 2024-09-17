'''Q2 – Faça um programa Python para ler uma seqüência de números inteiros – a leitura pára
quando o número zero for lido. No entanto, o usuário só deve poder digitar no máximo 150
números válidos. O programa deve imprimir as seguintes informações como resultado:
• A quantidade total de números negativos lidos.
• Os números positivos lidos cujos valores tiverem 4 dígitos significativos. A impressão
destes números deve mostrar primeiro os números menores que 5100, na mesma ordem
relativa em que foram lidos, e depois os maiores ou iguais a 5100, na ordem inversa da
que foram lidos.
• A média dos números positivos de 3 dígitos impressos no item anterior.
• O menor número negativo lido.
OBS1: Não pode usar as funções/métodos len, min, max, sum, nem sort.
Valor da questão: 3,5 '''

max = 10
n = int(input('Digite um número: '))
while (n == 0 ): #garantir que o usuário vai iniciar o programa
    n = int(input('Digite um número: '))

qtd_negativos = 0
c = 0
menor5100 = []
maior5100 = []
total = 0

while (n != 0) and (c<max):
    if n<0:
        qtd_negativos = qtd_negativos + 1
    
    menor_negativo = 0
    if n<menor_negativo:
        menor_negativo = n
    
    if n>0 and n>999 and n<=9999 and n<5100:
        menor5100.append(n)
    
    if n>0 and n>999 and n<=9999 and n>=5100:
        maior5100.append(n)
    
    n = int(input('Digite um número: '))
    c = c+1

qtd = 0
for i in maior5100:
    qtd = qtd+1
maior5100inv = []
for i in range(qtd-1, -1,-1):
    maior5100inv.append(maior5100[i])

print(f'A quantidade total de números negativos lidos é: {qtd_negativos}')
print(f'O menor número negativo lido é: {menor_negativo}')
print(f'números menores que 5100 {menor5100}')
print(f'números maiores que 5100 {maior5100inv}')

qtd = 0
for i in maior5100:
    qtd = qtd+1
maior5100inv = []
for i in range(qtd-1, -1,-1):
    maior5100inv.append(maior5100[i])
    
