from dispositivo import Dispositivo
from transitions import Machine

class Luz(Dispositivo):
    def __init__(self):
        """
        Inicializa uma instância da classe Luz, configurando a máquina de estados com os estados e transições
        específicos para o dispositivo Luz.
        """
        super().__init__()  # Chama o inicializador da classe base Dispositivo
        # Configura a máquina de estados para a Luz
        self.machine = Machine(
            model=self, 
            states=['desligada', 'ligada'],  # Define os estados possíveis
            initial='desligada'  # Estado inicial da máquina
        )
        # Adiciona a transição para ligar a Luz
        self.machine.add_transition(
            trigger='ligar',  # Gatilho para a transição
            source='desligada',  # Estado de origem
            dest='ligada'  # Estado de destino
        )
        # Adiciona a transição para desligar a Luz
        self.machine.add_transition(
            trigger='desligar',  # Gatilho para a transição
            source='ligada',  # Estado de origem
            dest='desligada'  # Estado de destino
        )

    def ligar(self):
        """
        Ativa a Luz, mudando o estado para 'ligada' ao acionar o gatilho 'ligar'.
        """
        self.trigger('ligar')  # Aciona a transição 'ligar'

    def desligar(self):
        """
        Desativa a Luz, mudando o estado para 'desligada' ao acionar o gatilho 'desligar'.
        """
        self.trigger('desligar')  # Aciona a transição 'desligar'

    def status(self):
        """
        Retorna o status atual da Luz com base no estado da máquina de estados.
        
        Returns:
            str: 'ligada' se o estado for 'ligada', caso contrário 'desligada'.
        """
        return 'ligada' if self.state == 'ligada' else 'desligada'

    def notificar(self):
        """
        Imprime o status atual da Luz para o console.
        """
        print(f"Luz está {self.status()}")  # Exibe o status da Luz
