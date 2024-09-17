from luz import Luz
from termostato import Termostato
from seguranca import SistemaSeguranca

class DispositivoFactory:
    """
    Fábrica de dispositivos para criar instâncias de diferentes tipos de dispositivos.
    Utiliza o padrão de projeto Factory Method para encapsular a lógica de criação de dispositivos.
    """

    @staticmethod
    def criar_dispositivo(tipo):
        """
        Método estático para criar um dispositivo com base no tipo fornecido.
        
        Args:
            tipo (str): O tipo do dispositivo a ser criado. Pode ser 'luz', 'termostato' ou 'seguranca'.
        
        Returns:
            Dispositivo: Uma instância do dispositivo correspondente ao tipo fornecido.
        
        Raises:
            ValueError: Se o tipo do dispositivo fornecido não for reconhecido.
        """
        if tipo == 'luz':
            return Luz()  # Retorna uma nova instância da classe Luz
        elif tipo == 'termostato':
            return Termostato()  # Retorna uma nova instância da classe Termostato
        elif tipo == 'seguranca':
            return SistemaSeguranca()  # Retorna uma nova instância da classe SistemaSeguranca
        else:
            raise ValueError("Tipo de dispositivo desconhecido.")  # Levanta uma exceção se o tipo não for reconhecido
