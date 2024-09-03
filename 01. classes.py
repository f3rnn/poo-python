import os

os.system("cls || clear") # Limpar terminal


class Aluno:
    def __init__(self, nome: str, idade: int) -> None :
        self.nome = nome
        self.idade = idade

    def exibir_dados(self) -> str:
        return f"Nome: {self.nome} \nIdade: {self.idade}"
    
aluno = Aluno("Marta", 22)

print(aluno.exibir_dados())