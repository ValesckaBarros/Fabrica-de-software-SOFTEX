import argparse
from casainteligente import CasaInteligente
from luz import Luz
from termostato import Termostato
from seguranca import SistemaSeguranca

# Inicializa o singleton da CasaInteligente
casa = CasaInteligente()

def adicionar_dispositivo(tipo):
    """
    Adiciona um dispositivo ao sistema com base no tipo fornecido.
    
    Args:
        tipo (str): O tipo do dispositivo a ser adicionado. Pode ser 'luz', 'termostato' ou 'seguranca'.
    """
    if tipo == 'luz':
        dispositivo = Luz()  # Cria uma nova instância da classe Luz
    elif tipo == 'termostato':
        dispositivo = Termostato()  # Cria uma nova instância da classe Termostato
    elif tipo == 'seguranca':
        dispositivo = SistemaSeguranca()  # Cria uma nova instância da classe SistemaSeguranca
    else:
        print(f"Tipo de dispositivo '{tipo}' desconhecido.")  # Mensagem de erro para tipo desconhecido
        return
    casa.adicionar_dispositivo(dispositivo)  # Adiciona o dispositivo à casa inteligente
    print(f"{tipo.capitalize()} adicionada.")  # Mensagem de confirmação

def listar_dispositivos():
    """
    Lista todos os dispositivos presentes no sistema.
    """
    casa.listar_dispositivos()  # Chama o método da casa inteligente para listar os dispositivos

def ligar_dispositivo(indice):
    """
    Liga um dispositivo pelo índice fornecido.
    
    Args:
        indice (int): O índice do dispositivo a ser ligado.
    """
    casa.ligar_dispositivo(indice)  # Chama o método da casa inteligente para ligar o dispositivo

def desligar_dispositivo(indice):
    """
    Desliga um dispositivo pelo índice fornecido.
    
    Args:
        indice (int): O índice do dispositivo a ser desligado.
    """
    casa.desligar_dispositivo(indice)  # Chama o método da casa inteligente para desligar o dispositivo

def remover_dispositivo(indice):
    """
    Remove um dispositivo pelo índice fornecido.
    
    Args:
        indice (int): O índice do dispositivo a ser removido.
    """
    casa.remover_dispositivo(indice)  # Chama o método da casa inteligente para remover o dispositivo

def ligar_todos_dispositivos():
    """
    Liga todos os dispositivos no sistema.
    """
    casa.ligar_todos_dispositivos()  # Chama o método da casa inteligente para ligar todos os dispositivos

def desligar_todos_dispositivos():
    """
    Desliga todos os dispositivos no sistema.
    """
    casa.desligar_todos_dispositivos()  # Chama o método da casa inteligente para desligar todos os dispositivos

def aquecer_termostato(indice):
    """
    Aquecer um termostato pelo índice fornecido.
    
    Args:
        indice (int): O índice do termostato a ser aquecido.
    """
    casa.aquecer_dispositivo(indice)  # Chama o método da casa inteligente para aquecer o termostato

def esfriar_termostato(indice):
    """
    Esfriar um termostato pelo índice fornecido.
    
    Args:
        indice (int): O índice do termostato a ser esfriado.
    """
    casa.esfriar_dispositivo(indice)  # Chama o método da casa inteligente para esfriar o termostato

def armar_seguranca_com_gente_em_casa(indice):
    """
    Arma o sistema de segurança com a configuração para gente em casa.
    
    Args:
        indice (int): O índice do sistema de segurança a ser armado.
    """
    casa.armar_com_gente_em_casa(indice)  # Chama o método da casa inteligente para armar a segurança com gente em casa

def armar_seguranca_sem_gente_em_casa(indice):
    """
    Arma o sistema de segurança com a configuração para sem gente em casa.
    
    Args:
        indice (int): O índice do sistema de segurança a ser armado.
    """
    casa.armar_sem_gente_em_casa(indice)  # Chama o método da casa inteligente para armar a segurança sem ninguém em casa

def main():
    """
    Função principal que processa os argumentos da linha de comando e executa as ações correspondentes.
    """
    parser = argparse.ArgumentParser(description="Gerenciador de Casa Inteligente")
    
    # Define os argumentos aceitos pela linha de comando
    parser.add_argument('--adicionar', type=str, choices=['luz', 'termostato', 'seguranca'], help="Adicionar um dispositivo")
    parser.add_argument('--listar', action='store_true', help="Listar todos os dispositivos")
    parser.add_argument('--ligar', type=int, help="Ligar um dispositivo pelo índice")
    parser.add_argument('--desligar', type=int, help="Desligar um dispositivo pelo índice")
    parser.add_argument('--remover', type=int, help="Remover um dispositivo pelo índice")
    parser.add_argument('--ligar_todos', action='store_true', help="Ligar todos os dispositivos")
    parser.add_argument('--desligar_todos', action='store_true', help="Desligar todos os dispositivos")
    parser.add_argument('--aquecer', type=int, help="Aquecer um termostato pelo índice")
    parser.add_argument('--esfriar', type=int, help="Esfriar um termostato pelo índice")
    parser.add_argument('--armar_com_gente_em_casa', type=int, help="Armar o sistema de segurança com gente em casa")
    parser.add_argument('--armar_sem_gente_em_casa', type=int, help="Armar o sistema de segurança sem gente em casa")

    args = parser.parse_args()  # Analisa os argumentos da linha de comando

    # Processa os argumentos e chama a função apropriada
    if args.adicionar:
        adicionar_dispositivo(args.adicionar)
    elif args.listar:
        listar_dispositivos()
    elif args.ligar is not None:
        ligar_dispositivo(args.ligar)
    elif args.desligar is not None:
        desligar_dispositivo(args.desligar)
    elif args.remover is not None:
        remover_dispositivo(args.remover)
    elif args.ligar_todos:
        ligar_todos_dispositivos()
    elif args.desligar_todos:
        desligar_todos_dispositivos()
    elif args.aquecer is not None:
        aquecer_termostato(args.aquecer)
    elif args.esfriar is not None:
        esfriar_termostato(args.esfriar)
    elif args.armar_com_gente_em_casa is not None:
        armar_seguranca_com_gente_em_casa(args.armar_com_gente_em_casa)
    elif args.armar_sem_gente_em_casa is not None:
        armar_seguranca_sem_gente_em_casa(args.armar_sem_gente_em_casa)
    else:
        print("Comando não reconhecido. Use '--help' para ver a lista de comandos.")

if __name__ == "__main__":
    main()
