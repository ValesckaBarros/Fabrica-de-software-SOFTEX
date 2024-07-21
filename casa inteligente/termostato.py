# termostato.py
from dispositivo import Dispositivo
from transitions import Machine

class Termostato(Dispositivo):
    def __init__(self):
        super().__init__()
        self.machine = Machine(model=self, states=['desligado', 'aquecendo', 'esfriando'], initial='desligado')
        self.machine.add_transition(trigger='ligar', source='desligado', dest='aquecendo')
        self.machine.add_transition(trigger='esfriar', source='aquecendo', dest='esfriando')
        self.machine.add_transition(trigger='aquecer', source='esfriando', dest='aquecendo')
        self.machine.add_transition(trigger='desligar', source=['aquecendo', 'esfriando'], dest='desligado')

    def ligar(self):
        self.trigger('ligar')

    def aquecer(self):
        self.trigger('aquecer')

    def esfriar(self):
        self.trigger('esfriar')

    def desligar(self):
        self.trigger('desligar')

    def status(self):
        return self.state

    def notificar(self):
        print(f"Termostato está {self.status()}")

