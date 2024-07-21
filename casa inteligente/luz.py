# luz.py
from dispositivo import Dispositivo
from transitions import Machine

class Luz(Dispositivo):
    def __init__(self):
        super().__init__()
        self.machine = Machine(model=self, states=['desligada', 'ligada'], initial='desligada')
        self.machine.add_transition(trigger='ligar', source='desligada', dest='ligada')
        self.machine.add_transition(trigger='desligar', source='ligada', dest='desligada')

    def ligar(self):
        self.trigger('ligar')

    def desligar(self):
        self.trigger('desligar')

    def status(self):
        return 'ligada' if self.state == 'ligada' else 'desligada'

    def notificar(self):
        print(f"Luz está {self.status()}")
