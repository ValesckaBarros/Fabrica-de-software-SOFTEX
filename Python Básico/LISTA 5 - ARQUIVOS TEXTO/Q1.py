'''1) Considere um arquivo texto cujo nome externo é 'discip.old' e que contém
informações de disciplinas (Código com 5 posições, nome com 35 posições e
créditos com 2 posições), uma disciplina por linha. Seu programa deve criar um
segundo arquivo com nome externo 'discip.new' contendo informações das
mesmas disciplinas, mas com as seguintes modificações:

(a) As disciplinas cujos códigos são IF125 e IF380 devem ser excluídas, i.e.,
não devem ser gravadas no novo arquivo.

(b) Os números de créditos das disciplinas cujos códigos começam por MA
devem ser alterados para 5.

(c) O novo arquivo terá um campo a mais (carga horária, com 3 posições)
cujo valor deve ser o número de créditos da disciplina multiplicado por 15.

No final o seu programa deve imprimir o número de disciplinas de cada arquivo e
ainda o número de disciplinas que tiveram seus números de créditos alterados.'''

arqEnt = open("Q1-arqDiscip.old", "r")
arqSai = open ('discip.new', 'w')
#for linha in arqEnt:
#     print(linha[6:36])

cont_ent = 0
cont_sai = 0
cont_mod = 0

for linha in arqEnt:
    cont_ent += 1
    codg = linha[0:5]
    nome = linha[6:36]
    cred = linha[42:44]
    if (codg == 'IF125') or (codg == 'IF380'):
        cont_mod += 1
    else:
        cont_sai += 1
        if codg[0:2]=='MA':
            arqSai.write('{:6}{:35}{:^5}{:5} \n'.format(codg, nome, '5', 5*15))
            cont_mod += 1
        else:
            arqSai.write('{:6}{:35}{:^5}{:5} \n'.format(codg, nome, cred, int(linha[42:44])*15))
    
print(f'Nº de disciplinas no arquivo de entrada: {cont_ent}')
print(f'Nº de disciplinas no arquivo de saída: {cont_sai}')
print(f'Nº de disciplinas modificadas/excluídas: {cont_mod}')



