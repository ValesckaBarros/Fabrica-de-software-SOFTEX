from dispositivo import Dispositivo
from transitions import Machine

class SistemaSeguranca(Dispositivo):
    def __init__(self):
        """
        Inicializa o Sistema de Segurança com estados e transições.
        """
        super().__init__()
        # Define a máquina de estados com os estados iniciais e possíveis transições
        self.machine = Machine(
            model=self,
            states=['desarmado', 'armado_com_gente_em_casa', 'armado_sem_ninguem_em_casa'],
            initial='desarmado'
        )
        # Adiciona transições para os estados
        self.machine.add_transition(
            trigger='armar_com_gente_em_casa',
            source='desarmado',
            dest='armado_com_gente_em_casa'
        )
        self.machine.add_transition(
            trigger='armar_sem_gente_em_casa',
            source=['desarmado', 'armado_com_gente_em_casa'],
            dest='armado_sem_ninguem_em_casa'
        )
        self.machine.add_transition(
            trigger='desarmar',
            source=['armado_com_gente_em_casa', 'armado_sem_ninguem_em_casa'],
            dest='desarmado'
        )

    def armar_com_gente_em_casa(self):
        """
        Transição para o estado 'armado_com_gente_em_casa'.
        """
        self.trigger('armar_com_gente_em_casa')

    def armar_sem_gente_em_casa(self):
        """
        Transição para o estado 'armado_sem_ninguem_em_casa'.
        """
        self.trigger('armar_sem_gente_em_casa')

    def desligar(self):
        """
        Transição para o estado 'desarmado'.
        """
        self.trigger('desarmar')

    def status(self):
        """
        Retorna o estado atual do sistema de segurança.
        """
        return self.state

    def notificar(self):
        """
        Imprime o status atual do sistema de segurança.
        """
        print(f"Sistema de segurança está {self.status()}")
