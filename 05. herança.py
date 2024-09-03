from abc import ABC, abstractmethod
import os

os.system("clear")

class Endereco:
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade

    def __str__(self) -> str:
        return (
            f"\nlogradouro: {self.logradouro}"
            f"\nnúmero: {self.numero}"
            f"\ncomplemento: {self.complemento}"
            f"\nCEP: {self.cep}"
            f"\ncidade: {self.cidade}"
                )


class Funcionario(ABC):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
    
    @abstractmethod
    def salario_final(self) -> float:
        pass

    def __str__(self) -> str:
        return (f"nome: {self.nome}"
                f"\ntelefone: {self.telefone}"
                f"\ne-mail: {self.email}"
                f"\nendereço: {self.endereco}"
                f"\nsalário: R${self.salario_final()}"
                )

class Engenheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, crea: str, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crea = crea

    def salario_final(self) -> float:
        return 2000.0
    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\ncrea: {self.crea}")

class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, crm: str, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crm = crm

    def salario_final(self) -> float:
        return 5000.0
    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\ncrm: {self.crm}")

engenheiro_1 = Engenheiro("Zezão", "71999999998", "zezão@gmail.com", "123456", Endereco("Alameda Rua", "123", "Ali na esquina", "40000-00", "Não Sei"))
print("\n=== engenheiro ===")
print(engenheiro_1)

medico_1 = Medico("James Bond", "71998999899", "bonddotigrao@gmail.com", "123456", Endereco("Avenida Alameda", "321", "Onde o vento faz curva", "40000-00", "Sei Não"))
print("\n=== medico ===")
print(medico_1)