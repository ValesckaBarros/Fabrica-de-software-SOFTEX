'''3. Ler 2 strings e dizer quantas vezes o primeiro aparece no segundo.'''

s1 = 'ana'
s2 = 'banana'

count = 0
c = 0
for j in range(len(s2)-len(s1)+1):
    a = ""
    for i in range(len(s1)):
        a += (s2[i+c])
    c += 1
    if a == s1:
        count += 1
    
print(f'a quantidade de vezes que {s1} aparece em {s2} é {count}')

    


    
    
        


   
    


    
