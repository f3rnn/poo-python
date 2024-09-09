import os
from enum import Enum

os.system("clear")

class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

class Pessoa:
    def __init__(self, nome: str, idade: int, sexo: Sexo) -> None:
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def __str__(self) -> str:
        return (f"Nome: {self.nome}"
               f"\nIdade: {self.idade}"
               f"\nSexo: {self.sexo.value}"
               )

pessoa_1 = Pessoa("marta", 22, Sexo.FEMININO)

print(pessoa_1)