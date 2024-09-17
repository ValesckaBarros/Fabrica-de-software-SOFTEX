'''1. Ler uma tabela com Cursos, onde:
• Cada curso é formado por um código (inteiro positivo), um nome (String), e o
centro a que pertence (inteiro positivo).
• A leitura da tabela de cursos pára com o código de curso zero.
• Depois o usuário fornecerá uma lista de códigos de centro para que o
programa imprima o código e nome de todos os cursos associados a cada
centro digitado.
• Se o código do centro não existir na tabela, mostrar a mensagem "Nenhum
curso encontrado" e continuar.
• O programa pára com a digitação de um código de centro inválido (negativo
ou zero).'''
tab = {}
cod = int(input('código: '))
while cod< 1:
    cod = int(input('código: '))

while cod !=0 :
    nome = input('nome: ')
    cen = int(input('centro: '))
    while cen < 1:
        cen = int(input('centro: '))
    tab[cod] = (nome, cen)
    cod = input('código: ')


    while cod<0:
        cod = int(input('código: '))

cen = int(input('centro: '))
while cen > 0:
    qtd = 0

    for ch in tab: 
        if cen == tab[ch][1]:
            print(ch, tab[ch][0])
            qtd += 1
    
    if qtd == 0: 
        print('nenhum')

    cen = int(input('centro: '))









