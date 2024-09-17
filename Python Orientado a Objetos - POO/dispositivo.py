from abc import ABC, abstractmethod

class Dispositivo(ABC):
    def __init__(self):
        """
        Inicializa a classe base Dispositivo.
        """
        self.machine = None  # Atributo para a máquina de estados, será definido nas subclasses

    @abstractmethod
    def status(self):
        """
        Método abstrato para obter o status do dispositivo.
        Deve ser implementado por subclasses.
        """
        pass

    @abstractmethod
    def notificar(self):
        """
        Método abstrato para notificar o status do dispositivo.
        Deve ser implementado por subclasses.
        """
        pass
