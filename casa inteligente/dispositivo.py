from abc import ABC, abstractmethod
from transitions import Machine

class Dispositivo(ABC):
    def __init__(self):
        self.machine = None

    @abstractmethod
    def status(self):
        pass

    @abstractmethod
    def notificar(self):
        pass
