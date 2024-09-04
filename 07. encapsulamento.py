from abc import ABC, abstractmethod
import os

os.system("clear")

class SalarioNegativoError(Exception):
    pass

class Endereco:
    def __init__(self, logradouro: str, numero: str, cidade: str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.cidade = cidade
    
    def  __str__(self) -> str:
        return (
            f"\nlogradouro: {self.logradouro}"
            f"\nnúmero: {self.numero}"
            f"\ncidade: {self.cidade}"
                )
class Funcionario(ABC):
    def __init__(self, nome: str, email: str, salario: float, endereco: Endereco) -> None:
        self.verificar_salario(salario)
        self.nome = nome
        self.email = email
        self.salario = salario
        self.endereco = endereco
    
    @abstractmethod
    def salario_final(self) -> float:
        pass

    def verificar_salario(self, valor):
        try:
            self.mensagem(valor)
        except SalarioNegativoError as e:
            return f"erro: {e}"

    def mensagem(self, valor):
        if valor < 0:
            raise SalarioNegativoError("valor inválido")

    def __str__(self) -> str:
        return (
            f"\nnome: {self.nome}"
            f"\ne-mail: {self.email}"
            f"\nsalário: {self.verificar_salario(self.salario)}"
            f"\nendereço: {self.endereco}"
                )

class Motoboy(Funcionario):
    def __init__(self, nome: str, email: str, salario: float, cnh: str, endereco: Endereco) -> None:
        super().__init__(nome, email, salario, endereco)
        self.cnh = cnh
    
    def salario_final(self) -> float:
        return self.salario
    
    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nCNH: {self.cnh}")

class Gerente(Funcionario):
    def salario_final(self) -> float:
        salarioFinal = self.verificar_salario(self.salario)
        return salarioFinal

gerente_1 = Gerente("zezão", "zezão@gmail", 1400.0, Endereco("alameda rua", "123", "não sei"))
print(gerente_1)

motoboy_1 = Motoboy("james bond", "bonddotigrão@gmail.com", -1400.0, "123456", Endereco("rua alameda", "321", "sei não"))
print(motoboy_1)