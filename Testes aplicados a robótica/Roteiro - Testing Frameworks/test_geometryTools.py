from geometryTools import GeometryTools 
import pytest

class Test_geometryTools():

    skipFourAxis = True

    # Executado uma vez antes de todos os testes na classe.
    # Configurações gerais que serão usadas em todos os testes.
    def setup_class(self):
        print('setup executado 1 unica vez')
        self.gt = GeometryTools() # Instancia a classe GeometryTools para ser usada nos testes

    # Executado antes de cada teste.
    # Garante que uma nova instância de 'geometryTools' 
    # seja criada para cada teste, para evitar que testes 
    # compartilhem o mesmo estado.
    def setup_method(self):
        print('Nova instancia de geometryTools foi criada')
        self.calc = GeometryTools()  
    
    # Executado uma vez após todos os testes da classe.
    def teardown_class(self):
        print('instancia da classe compartinhada geometryTools DELETADA')
        del self.gt  # Remove a instância compartilhada

    # Executado após cada teste individual.
    def teardown_method(self):
        print('Instância de geometryTools foi DELETADA')
        del self.calc  # Remove a instância individual usada no teste

    def test_rectangleArea(self):
        assert self.gt.rectangleArea(4, 2) == 8

    @pytest.mark.parametrize("largura, altura, esperado", [
        (4, 2, 12),
        (5, 3, 16),
        (7, 10, 34),
        (2, 3, 10)
    ])
    def test_rectanglePerimeter(self, largura, altura, esperado):
        assert self.gt.rectanglePerimeter(largura, altura) == esperado

    def test_triangleArea(self):
        assert self.gt.triangleArea(4, 2) == 4

    # Ignorando este teste
    @pytest.mark.skipif(skipFourAxis, reason="Ignorando o teste do perímetro do triângulo")  
    def test_trianglePerimeter(self):
        assert self.gt.trianglePerimeter(5,5,5) == 15 
    
    def test_circleArea(self):
        assert self.gt.circleArea(2) == 12.56

    def test_circlePerimeter(self):
        assert self.gt.circlePerimeter(2)== 12.56
    
    # Testa se o método 'circleArea' da classe geometryTools 
    # lança uma exceção TypeError ao tentar inserir um caracter 
    # no lugar do raio. Usa a função pytest.raises para esperar 
    # a exceção.
    def test_circleArea_invalid_input(self):
        with pytest.raises(TypeError):
            self.gt.circleArea('a')
    

    
    



