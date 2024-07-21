class Observer:
    def atualizar(self, dispositivo):
        if dispositivo:
            print(f"Observer notificado: {dispositivo.__class__.__name__} está {dispositivo.status()}")
        else:
            print("Observer notificado: Dispositivo removido.")
