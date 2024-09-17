from calculator import Calculator
import pytest

class TestCalculator():

    skipFourAxis = True
    
    # Executado uma vez antes de todos os testes na classe.
    # Configurações gerais que serão usadas em todos os testes.
    def setup_class(self):
        print('setup executado 1 unica vez')
        # Instancia a classe Calculator para ser usada nos testes
        self.calc = Calculator()
    
    # Executado uma vez após todos os testes na classe.
    # Serve para limpar recursos ou fazer uma limpeza geral.
    def teardown_class(self):
        print('cleanup executado uma vez')
    
    # Executado antes de cada teste.
    # Garante que uma nova instância de 'Calculator' seja criada para cada teste,
    # para evitar que testes compartilhem o mesmo estado.
    def setup_method(self):
        print('setup executado antes de cada teste')
        self.calc = Calculator()  # Instancia a classe Calculator para cada teste
    
    # Executado após cada teste.
    # Serve para liberar recursos alocados durante o teste.
    def teardown_method(self):
        print('clean up executado após cada teste')

    # Testa o método 'addiction' da classe Calculator.
    # Verifica se a soma de 2 + 2 é igual a 4.

    def test_add(self):
        assert self.calc.addiction(2, 2) == 4

    #@pytest.mark.skipif(condition, *, reason = None)
    @pytest.mark.skipif(skipFourAxis, reason = 'duplicate')
    def test_add2(self):
        assert self.calc.addiction(2, 2) == 4



    '''Esse código utiliza o decorador @pytest.mark.parametrize 
    da biblioteca pytest para criar testes parametrizados. Isso 
    permite testar um mesmo método com diferentes conjuntos de 
    valores de entrada de maneira eficiente, evitando a repetição 
    de código.'''
    @pytest.mark.parametrize("a, b, expected",[(2,2,4), (5,5,10), (2,9,11)] )
    def test_sum_generic(self, a, b, expected):
        assert self.calc.addiction(a,b) == expected

    

    # Testa o método 'subtraction' da classe Calculator.
    # Verifica se a subtração de 4 - 2 é igual a 2.
    def test_sub(self):
        assert self.calc.subtraction(4, 2) == 2
    
    # Testa o método 'multiplication' da classe Calculator.
    # Verifica se a multiplicação de 4 * 2 é igual a 8.
    def test_mul(self):
        assert self.calc.multiplication(4, 2) == 8
    
    # Testa o método 'division' da classe Calculator.
    # Verifica se a divisão de 4 / 2 é igual a 2.
    def test_div(self):
        assert self.calc.division(4, 2) == 2
    
    # Testa se o método 'division' da classe Calculator lança uma exceção ZeroDivisionError
    # ao tentar dividir por zero. Usa a função pytest.raises para esperar a exceção.
    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(4, 0)
