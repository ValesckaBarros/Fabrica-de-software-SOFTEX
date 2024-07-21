# seguranca.py

from dispositivo import Dispositivo
from transitions import Machine

class SistemaSeguranca(Dispositivo):
    def __init__(self):
        super().__init__()
        self.machine = Machine(model=self, states=['desarmado', 'armado_com_gente_em_casa', 'armado_sem_ninguem_em_casa'], initial='desarmado')
        self.machine.add_transition(trigger='armar_com_gente_em_casa', source='desarmado', dest='armado_com_gente_em_casa')
        self.machine.add_transition(trigger='armar_sem_gente_em_casa', source=['desarmado', 'armado_com_gente_em_casa'], dest='armado_sem_ninguem_em_casa')
        self.machine.add_transition(trigger='desarmar', source=['armado_com_gente_em_casa', 'armado_sem_ninguem_em_casa'], dest='desarmado')

    def armar_com_gente_em_casa(self):
        self.trigger('armar_com_gente_em_casa')

    def armar_sem_gente_em_casa(self):
        self.trigger('armar_sem_gente_em_casa')

    def desligar(self):
        self.trigger('desarmar')

    def status(self):
        return self.state

    def notificar(self):
        print(f"Sistema de segurança está {self.status()}")
