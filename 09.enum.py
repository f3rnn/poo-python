import os
from enum import Enum

os.system("clear")

class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

class Setor (Enum):
    FINANCEIRO = "Financeiro"
    RECURSOS_HUMANOS = "Recursos Humanos"
    VENDAS = "Vendas"
    MARKETING = "Marketing"

class Funcionario:
    def __init__(self, id: int, nome: str, idade: int, salario: float, setor: Setor, sexo: Sexo) -> None:
        self.id = id
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.setor = setor
        self.sexo = sexo
    
    def __str__(self) -> str:
        return (f"ID: {self.id}"
                f"\nnome: {self.nome}"
                f"\nidade: {self.idade}"
                f"\nsalario: R${self.salario}"
                f"\nsetor: {self.setor.value}"
                f"\nsexo: {self.sexo.value}"
                )
    
funcionario_um = Funcionario(123, "Zezão", 20, 5000.0, Setor.FINANCEIRO, Sexo.MASCULINO)
print(funcionario_um)