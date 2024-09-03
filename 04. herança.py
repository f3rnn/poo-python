from abc import ABC, abstractmethod
import os

os.system("clear")

class Funcionario(ABC):
    def __init__(self, nome: str, idade: int, salario: float) -> None:
        self.nome = nome
        self.idade = idade
        self.salario = salario

    @abstractmethod
    def calcular_salario(self) -> float:
        pass

class Gerente(Funcionario):
    def calcular_salario(self) -> float:
        BONIFICACAO = 1.2
        salarioFinal = self.salario * BONIFICACAO
        return salarioFinal

class Motoboy(Funcionario):
    def __init__(self, nome: str, idade: int, salario: float, cnh: str) -> None:
        super().__init__(nome, idade, salario)
        self.cnh = cnh
    
    def calcular_salario(self) -> float:
        BONIFICACAO = 1.1
        salarioFinal = self.salario * BONIFICACAO
        return salarioFinal

gerente = Gerente("marta", 22, 2000.0)
print(f"nome: {gerente.nome}")
print(f"idade: {gerente.idade}")
print(f"salário: {gerente.calcular_salario()}")

motoboy = Motoboy("josé", 33, 1000.0, "123456")
print(f"nome: {motoboy.nome}")
print(f"idade: {motoboy.idade}")
print(f"cnh: {motoboy.cnh}")
print(f"salário: {motoboy.calcular_salario}")