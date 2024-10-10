from abc import ABC, classmethod, abstractmethod
from datetime import datetime

class Conta:
    def __init__(self, cliente, numero):
        self._cliente = cliente
        self._agencia = '0001'
        self._numero = numero
        self._saldo = 0
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > 0:
            self._saldo -= valor
            print("Saque realizado com sucesso!")
            return True
        else:
            print("Operação falhou! O valor informado é inválido.")
        
        return False
    
    def depositar(self, valor):
        if valor > 0:
            saldo += valor
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

class Historico:
    pass

class ContaCorrente(Conta):
    pass

class Transação(ABC):
    pass

class Deposito(Transação):
    pass

class Saque(Transação):
    pass

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf