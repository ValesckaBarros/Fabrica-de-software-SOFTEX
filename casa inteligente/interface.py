# interface.py

from casainteligente import CasaInteligente
from fabricadispositivos import DispositivoFactory
from observer import Observer

def exibir_menu():
    print("\nDigite um comando (ou 'sair' para encerrar):")
    print("1. listar_dispositivos")
    print("2. adicionar_luz")
    print("3. adicionar_termostato")
    print("4. adicionar_seguranca")
    print("5. ligar_dispositivo <índice>")
    print("6. desligar_dispositivo <índice>")
    print("7. remover_dispositivo <índice>")
    print("8. ligar_todos_dispositivos")
    print("9. desligar_todos_dispositivos")
    print("10. aquecer_termostato <índice>")
    print("11. esfriar_termostato <índice>")
    print("12. armar_seguranca_com_gente_em_casa <índice>")
    print("13. armar_seguranca_sem_gente_em_casa <índice>")
    print("14. help")

def main():
    casa = CasaInteligente()
    observador = Observer()
    casa.adicionar_observador(observador)

    exibir_menu()  # Exibir menu uma vez no início

    while True:
        comando = input("Digite um comando (ou 'help' para o menu, 'sair' para encerrar): ").strip()

        if comando == 'sair':
            break
        elif comando == 'help':
            exibir_menu()
        elif comando == 'listar_dispositivos':
            casa.listar_dispositivos()
        elif comando == 'adicionar_luz':
            casa.adicionar_dispositivo(DispositivoFactory.criar_dispositivo('luz'))
        elif comando == 'adicionar_termostato':
            casa.adicionar_dispositivo(DispositivoFactory.criar_dispositivo('termostato'))
        elif comando == 'adicionar_seguranca':
            casa.adicionar_dispositivo(DispositivoFactory.criar_dispositivo('seguranca'))
        elif comando.startswith('ligar_dispositivo'):
            _, idx = comando.split()
            casa.ligar_dispositivo(int(idx))
        elif comando.startswith('desligar_dispositivo'):
            _, idx = comando.split()
            casa.desligar_dispositivo(int(idx))
        elif comando.startswith('remover_dispositivo'):
            _, idx = comando.split()
            casa.remover_dispositivo(int(idx))
        elif comando == 'ligar_todos_dispositivos':
            casa.ligar_todos_dispositivos()
        elif comando == 'desligar_todos_dispositivos':
            casa.desligar_todos_dispositivos()
        elif comando.startswith('aquecer_termostato'):
            _, idx = comando.split()
            casa.aquecer_dispositivo(int(idx))
        elif comando.startswith('esfriar_termostato'):
            _, idx = comando.split()
            casa.esfriar_dispositivo(int(idx))
        elif comando.startswith('armar_seguranca_com_gente_em_casa'):
            _, idx = comando.split()
            casa.armar_com_gente_em_casa(int(idx))
        elif comando.startswith('armar_seguranca_sem_gente_em_casa'):
            _, idx = comando.split()
            casa.armar_sem_gente_em_casa(int(idx))
        else:
            print("Comando não reconhecido.")

if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
