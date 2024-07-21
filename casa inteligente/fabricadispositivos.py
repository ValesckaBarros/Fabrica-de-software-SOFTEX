from luz import Luz
from termostato import Termostato
from seguranca import SistemaSeguranca

class DispositivoFactory:
    @staticmethod
    def criar_dispositivo(tipo):
        if tipo == 'luz':
            return Luz()
        elif tipo == 'termostato':
            return Termostato()
        elif tipo == 'seguranca':
            return SistemaSeguranca()
        else:
            raise ValueError("Tipo de dispositivo desconhecido.")
