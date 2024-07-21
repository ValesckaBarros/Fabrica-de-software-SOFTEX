# casainteligente.py

from seguranca import SistemaSeguranca
from termostato import Termostato
from functools import reduce

class CasaInteligente:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(CasaInteligente, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'dispositivos'):
            self.dispositivos = []
        if not hasattr(self, 'observadores'):
            self.observadores = []

    def adicionar_dispositivo(self, dispositivo):
        self.dispositivos.append(dispositivo)
        self.notificar_observadores(dispositivo)

    def remover_dispositivo(self, index):
        if 0 <= index < len(self.dispositivos):
            dispositivo = self.dispositivos.pop(index)
            self.notificar_observadores(dispositivo)

    def listar_dispositivos(self):
        if self.dispositivos:
            dispositivos_status = map(lambda d: f"{self.dispositivos.index(d)}: {d.__class__.__name__} está {d.status()}", self.dispositivos)
            for status in dispositivos_status:
                print(status)
        else:
            print("Nenhum dispositivo encontrado.")

    def ligar_dispositivo(self, index):
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
        if 0 <= index < len(self.dispositivos):
            dispositivo = self.dispositivos[index]
            dispositivo.desligar()
            self.notificar_observadores(dispositivo)
        else:
            print("Índice de dispositivo inválido.")

    def aquecer_dispositivo(self, index):
        if 0 <= index < len(self.dispositivos) and isinstance(self.dispositivos[index], Termostato):
            self.dispositivos[index].aquecer()
            self.notificar_observadores(self.dispositivos[index])
        else:
            print("Índice de dispositivo inválido ou dispositivo não é um termostato.")

    def esfriar_dispositivo(self, index):
        if 0 <= index < len(self.dispositivos) and isinstance(self.dispositivos[index], Termostato):
            self.dispositivos[index].esfriar()
            self.notificar_observadores(self.dispositivos[index])
        else:
            print("Índice de dispositivo inválido ou dispositivo não é um termostato.")

    def armar_com_gente_em_casa(self, index):
        if 0 <= index < len(self.dispositivos) and isinstance(self.dispositivos[index], SistemaSeguranca):
            self.dispositivos[index].armar_com_gente_em_casa()
            self.notificar_observadores(self.dispositivos[index])
        else:
            print("Índice de dispositivo inválido ou dispositivo não é um sistema de segurança.")

    def armar_sem_gente_em_casa(self, index):
        if 0 <= index < len(self.dispositivos) and isinstance(self.dispositivos[index], SistemaSeguranca):
            self.dispositivos[index].armar_sem_gente_em_casa()
            self.notificar_observadores(self.dispositivos[index])
        else:
            print("Índice de dispositivo inválido ou dispositivo não é um sistema de segurança.")

    def ligar_todos_dispositivos(self):
        def ligar_dispositivo(acc, dispositivo):
            if isinstance(dispositivo, SistemaSeguranca):
                dispositivo.armar_com_gente_em_casa()
            else:
                dispositivo.ligar()
            self.notificar_observadores(dispositivo)
            return acc

        reduce(ligar_dispositivo, self.dispositivos, None)

    def desligar_todos_dispositivos(self):
        def desligar_dispositivo(acc, dispositivo):
            dispositivo.desligar()
            self.notificar_observadores(dispositivo)
            return acc

        reduce(desligar_dispositivo, self.dispositivos, None)

    def adicionar_observador(self, observador):
        self.observadores.append(observador)

    def notificar_observadores(self, dispositivo):
        for observador in self.observadores:
            observador.atualizar(dispositivo)

