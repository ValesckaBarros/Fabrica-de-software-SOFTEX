from seguranca import SistemaSeguranca
from termostato import Termostato
from functools import reduce

class CasaInteligente:
    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        Implementa o padrão Singleton para garantir que apenas uma instância da CasaInteligente seja criada.
        """
        if not cls._instance:
            cls._instance = super(CasaInteligente, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        """
        Inicializa a lista de dispositivos e observadores se ainda não estiverem definidos.
        """
        if not hasattr(self, 'dispositivos'):
            self.dispositivos = []
        if not hasattr(self, 'observadores'):
            self.observadores = []

    def adicionar_dispositivo(self, dispositivo):
        """
        Adiciona um dispositivo à lista de dispositivos e notifica os observadores.
        
        :param dispositivo: Instância do dispositivo a ser adicionado.
        """
        self.dispositivos.append(dispositivo)
        self.notificar_observadores(dispositivo)

    def remover_dispositivo(self, index):
        """
        Remove um dispositivo da lista de dispositivos com base no índice e notifica os observadores.
        
        :param index: Índice do dispositivo a ser removido.
        """
        if 0 <= index < len(self.dispositivos):
            dispositivo = self.dispositivos.pop(index)
            self.notificar_observadores(dispositivo)
        else:
            print("Índice de dispositivo inválido.")

    def listar_dispositivos(self):
        """
        Lista todos os dispositivos e seus estados. Utiliza a função map para criar uma lista de status dos dispositivos.
        """
        if self.dispositivos:
            # Usando map para criar uma lista de strings representando o status dos dispositivos
            dispositivos_status = map(lambda d: f"{self.dispositivos.index(d)}: {d.__class__.__name__} está {d.status()}", self.dispositivos)
            # Convertendo o map object em uma lista e iterando para imprimir cada status
            for status in dispositivos_status:
                print(status)
        else:
            print("Nenhum dispositivo encontrado.")

    def ligar_dispositivo(self, index):
        """
        Liga um dispositivo com base no índice. Se o dispositivo for um SistemaSeguranca, ele será armado com gente em casa.
        
        :param index: Índice do dispositivo a ser ligado.
        """
        if 0 <= index < len(self.dispositivos):
            dispositivo = self.dispositivos[index]
            if isinstance(dispositivo, SistemaSeguranca):
                dispositivo.armar_com_gente_em_casa()
            else:
                dispositivo.ligar()
            self.notificar_observadores(dispositivo)
        else:
            print("Índice de dispositivo inválido.")

    def desligar_dispositivo(self, index):
        """
        Desliga um dispositivo com base no índice.
        
        :param index: Índice do dispositivo a ser desligado.
        """
        if 0 <= index < len(self.dispositivos):
            dispositivo = self.dispositivos[index]
            dispositivo.desligar()
            self.notificar_observadores(dispositivo)
        else:
            print("Índice de dispositivo inválido.")

    def aquecer_dispositivo(self, index):
        """
        Aciona o aquecimento de um termostato com base no índice.
        
        :param index: Índice do dispositivo a ser aquecido.
        """
        if 0 <= index < len(self.dispositivos) and isinstance(self.dispositivos[index], Termostato):
            self.dispositivos[index].aquecer()
            self.notificar_observadores(self.dispositivos[index])
        else:
            print("Índice de dispositivo inválido ou dispositivo não é um termostato.")

    def esfriar_dispositivo(self, index):
        """
        Aciona o resfriamento de um termostato com base no índice.
        
        :param index: Índice do dispositivo a ser esfriado.
        """
        if 0 <= index < len(self.dispositivos) and isinstance(self.dispositivos[index], Termostato):
            self.dispositivos[index].esfriar()
            self.notificar_observadores(self.dispositivos[index])
        else:
            print("Índice de dispositivo inválido ou dispositivo não é um termostato.")

    def armar_com_gente_em_casa(self, index):
        """
        Arma o sistema de segurança com a presença de pessoas em casa com base no índice.
        
        :param index: Índice do dispositivo a ser armado.
        """
        if 0 <= index < len(self.dispositivos) and isinstance(self.dispositivos[index], SistemaSeguranca):
            self.dispositivos[index].armar_com_gente_em_casa()
            self.notificar_observadores(self.dispositivos[index])
        else:
            print("Índice de dispositivo inválido ou dispositivo não é um sistema de segurança.")

    def armar_sem_gente_em_casa(self, index):
        """
        Arma o sistema de segurança sem a presença de pessoas em casa com base no índice.
        
        :param index: Índice do dispositivo a ser armado.
        """
        if 0 <= index < len(self.dispositivos) and isinstance(self.dispositivos[index], SistemaSeguranca):
            self.dispositivos[index].armar_sem_gente_em_casa()
            self.notificar_observadores(self.dispositivos[index])
        else:
            print("Índice de dispositivo inválido ou dispositivo não é um sistema de segurança.")

    def ligar_todos_dispositivos(self):
        """
        Liga todos os dispositivos usando reduce para aplicar a operação de ligar em cada dispositivo.
        """
        # Usando reduce para aplicar a operação de ligar em todos os dispositivos
        def ligar_dispositivo(acc, dispositivo):
            if isinstance(dispositivo, SistemaSeguranca):
                dispositivo.armar_com_gente_em_casa()
            else:
                dispositivo.ligar()
            self.notificar_observadores(dispositivo)
            return acc

        reduce(ligar_dispositivo, self.dispositivos, None)

    def desligar_todos_dispositivos(self):
        """
        Desliga todos os dispositivos usando reduce para aplicar a operação de desligar em cada dispositivo.
        """
        # Usando reduce para aplicar a operação de desligar em todos os dispositivos
        def desligar_dispositivo(acc, dispositivo):
            dispositivo.desligar()
            self.notificar_observadores(dispositivo)
            return acc

        reduce(desligar_dispositivo, self.dispositivos, None)

    def adicionar_observador(self, observador):
        """
        Adiciona um observador à lista de observadores.

        :param observador: Instância do observador a ser adicionado.
        """
        self.observadores.append(observador)

    def notificar_observadores(self, dispositivo):
        """
        Notifica todos os observadores sobre o status do dispositivo.

        :param dispositivo: Instância do dispositivo que sofreu uma mudança de status.
        """
        for observador in self.observadores:
            observador.atualizar(dispositivo)
