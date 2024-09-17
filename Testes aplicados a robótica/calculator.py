class Calculator:
    def addiction(self, n1, n2):
        return n1+n2
    def subtraction(self, n1, n2):
        return n1-n2
    def multiplication(self, n1, n2):
        return n1*n2
    def division(self, n1, n2):
        return n1/n2
    
if __name__ == '__main__':
    calc = Calculator()
    #teste1
    esperado = 4
    observado = calc.addiction(2,2)
    if observado == esperado:
        print('Passou')
    else:
        print('Falhou')

    #teste2
    esperado = 2
    observado = calc.subtraction(4,2)
    if observado == esperado:
        print('Passou')
    else:
        print('Falhou')