'''Q1 – Faça uma função Python para calcular a soma dos N primeiros termos da série abaixo. O
valor de N deve ser um parâmetro e a função deve retornar zero como resultado caso o
número de termos não seja positivo.
S = 10 / 1 – 15 / 5 + 20 / 8 – 25 / 11 + 30 / 15 – 35 / 17 + ...
Escrever também um programa principal para perguntar ao usuário a quantidade de vezes
(qtd) que ele deseja calcular o valor da série e, em seguida, os números de termos desejados
nestas qtd vezes. Para cada um deles, seu programa deve usar a função e imprimir o resultado
da série (com 4 casas decimais), da seguinte forma: “O valor da série com ... termos é ...”. '''

def serie(n):
    if n < 0:
        return 0
    else:
        s = 0
        d = 10
        n1 = 1
        n2 = 5
        for i in range(1, n+1):
            if i%2 != 0:
                a = d/n1
                s = s+a
                d = d+5
                n1 = n1+7
            else:
                a = d/n2
                s = s-a
                d = d+5
                n2 = (n2+6)
        return s

nserie = int(input('digite a quantidade de vezes que deseja calcular a série: '))
while nserie<=0:
    nserie = int(input('digite a quantidade de vezes que deseja calcular a série: '))

for i in range(nserie):
    ntermos = int(input('digite a quantidade de termos da série: '))
    resultado = serie(ntermos)
    print(f'O valor da série com {ntermos} termos é {resultado:.4f}')




