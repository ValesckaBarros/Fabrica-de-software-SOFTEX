from dispositivo import Dispositivo
from transitions import Machine

class Termostato(Dispositivo):
    def __init__(self):
        """
        Inicializa o termostato e define sua máquina de estados.
        """
        super().__init__()
        # Define os estados e a máquina de estados para o termostato
        self.machine = Machine(model=self, states=['desligado', 'aquecendo', 'esfriando'], initial='desligado')
        # Adiciona transições entre os estados
        self.machine.add_transition(trigger='ligar', source='desligado', dest='aquecendo')
        self.machine.add_transition(trigger='esfriar', source='aquecendo', dest='esfriando')
        self.machine.add_transition(trigger='aquecer', source='esfriando', dest='aquecendo')
        self.machine.add_transition(trigger='desligar', source=['aquecendo', 'esfriando'], dest='desligado')

    def ligar(self):
        """
        Transita o termostato do estado 'desligado' para 'aquecendo'.
        """
        self.trigger('ligar')

    def aquecer(self):
        """
        Transita o termostato do estado 'esfriando' para 'aquecendo'.
        """
        self.trigger('aquecer')

    def esfriar(self):
        """
        Transita o termostato do estado 'aquecendo' para 'esfriando'.
        """
        self.trigger('esfriar')

    def desligar(self):
        """
        Transita o termostato dos estados 'aquecendo' ou 'esfriando' para 'desligado'.
        """
        self.trigger('desligar')

    def status(self):
        """
        Retorna o estado atual do termostato.
        """
        return self.state

    def notificar(self):
        """
        Imprime o status atual do termostato.
        """
        print(f"Termostato está {self.status()}")


