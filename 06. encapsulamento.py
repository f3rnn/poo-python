import os

os.system("clear")

class SaldoInsuficienteError(Exception):
    pass

class DepositoNegativoError(Exception):
    pass

class Conta:
    def __init__(self, numero_conta: int, agencia: int) -> None:
        self.numero_conta = numero_conta
        self.agencia = agencia
        self._saldo = 0 #atributo protegido

    @property
    def saldo(self):
        return self._saldo
    
    def sacar(self, valor) -> float:
        try:
            self.__verificar_sacar(valor)
        except SaldoInsuficienteError as error:
            return f"erro: {error}"

        self._saldo -= valor
        return self._saldo
    
    def __verificar_sacar(self, valor): #metodo privado
        if valor > self.saldo:
            raise  SaldoInsuficienteError("saldo insuficiente") #lançando errro

    def depositar(self, valor):
        try:
            self.__verificar_depositar(valor)
        except DepositoNegativoError as error:
            return f"erro: {error}"
        
        self._saldo += valor
        return self._saldo
    
    def __verificar_depositar(self, valor):
        if valor < 0:
            raise DepositoNegativoError("valor inválido")

class ContaCorrente(Conta):
    pass

class ContaPoupanca(Conta):
    pass

conta_corrente = ContaCorrente(222, 333)
conta_poupanca = ContaPoupanca(444, 555)

#print(conta_corrente._saldo)
print(conta_corrente.saldo)
print(conta_corrente.sacar(200))
print(conta_corrente.saldo)
print(conta_corrente.depositar(-1))