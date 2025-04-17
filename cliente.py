class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)
