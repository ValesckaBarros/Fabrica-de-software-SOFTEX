from abc import ABC, abstractmethod

class Dispositivo(ABC):
    """
    Classe abstrata que define a interface comum para todos os dispositivos.
    Utiliza a biblioteca `abc` para implementar uma classe base abstrata.
    """

    def __init__(self):
        """
        Inicializa o dispositivo.
        """
        self.machine = None
        # Atributo `machine` pode ser utilizado para associar uma máquina de estados (

