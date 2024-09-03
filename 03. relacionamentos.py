import os

os.system("cls || clear") # Limpar terminal

class Endereco:
    def __init__(self, logradouro: str, numero: int) -> None: 
        self.logradouro = logradouro
        self.numero = numero

    def __str__ (self) -> str:
         return f"Logradouro: {self.logradouro} \nNúmero: {self.numero}"


class Aluno:
    def __init__(self, nome: str, idade: int, endereco: Endereco) -> None :
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def __str__ (self) -> str:
        return f"Nome: {self.nome} \nIdade: {self.idade} \nDados do endereço: \n{self.endereco}"
    
    
# Instanciar classe: 
aluno = Aluno("Marta", 22, Endereco("Rua G", 9))

print(aluno)