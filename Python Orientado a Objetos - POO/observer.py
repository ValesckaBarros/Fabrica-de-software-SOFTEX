class Observer:
    def atualizar(self, dispositivo):
        """
        Atualiza o estado do observador com base no dispositivo notificado.
        
        Args:
            dispositivo (Dispositivo): O dispositivo que acionou a notificação. Pode ser None se o dispositivo for removido.
        """
        if dispositivo:
            # Se o dispositivo não for None, imprime o status atual do dispositivo
            print(f"Observer notificado: {dispositivo.__class__.__name__} está {dispositivo.status()}")
        else:
            # Se o dispositivo for None, indica que o dispositivo foi removido
            print("Observer notificado: Dispositivo removido.")

