# 💳 Sistema Bancário em POO com Python

Projeto prático desenvolvido na plataforma [DIO](https://www.dio.me/) para praticar conceitos de **Programação Orientada a Objetos (POO)** utilizando Python.

## 🧠 Conceitos aplicados
- Classes e Objetos
- Herança
- Encapsulamento
- Polimorfismo
- Instância de classes e métodos

## 🧱 Estrutura do Projeto
projeto_banco/ ├── banco.py ├── cliente.py ├── conta.py ├── conta_corrente.py └── main.py


## ⚙️ Funcionalidades
- Criar clientes
- Criar contas comuns e contas correntes com limite especial
- Realizar depósitos e saques
- Exibir saldo da conta
- Registrar múltiplas contas por cliente
- Banco que gerencia todos os clientes e contas

## 💻 Exemplo de uso
```python
cliente = Cliente("Rafael")
conta = ContaCorrente(101, cliente, limite=500)

conta.depositar(300)
conta.sacar(700)  # Usa limite especial
conta.exibir_saldo()
# Saída: Saldo da conta 101: R$ -400.00