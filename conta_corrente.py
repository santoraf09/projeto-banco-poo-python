from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500):
        super().__init__(numero, cliente)
        self.limite = limite

    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            return True
        return False