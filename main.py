from cliente import Cliente
from conta_corrente import ContaCorrente
from banco import Banco

cliente1 = Cliente("Rafael")
conta1 = ContaCorrente(101, cliente1, limite=500)

cliente1.adicionar_conta(conta1)

conta1.depositar(300)
conta1.sacar(700)  # Testando o limite especial
conta1.exibir_saldo()