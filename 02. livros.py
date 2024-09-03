import os

os.system("cls || clear")

class DadosDoLivro:
    def __init__(self, titulo: str, autor: str, numeroDePaginas: int, preco: float) -> None:
        self.titulo = titulo
        self.autor = autor
        self.numeroDePaginas = numeroDePaginas
        self.preco = preco
        
    def exibir_dados(self) -> str:
        return f"Título: {self.titulo} \nAutor: {self.autor} \nNúmero de páginas: {self.numeroDePaginas} \nPreço: {self.preco}"

PrimeiroLivro = DadosDoLivro("A cor que caiu do espaço", "H.P Lovecraft", 144, 29.58)
SegundoLivro = DadosDoLivro("O chamado de Cthulhu", "H.P Lovecraft", 160, 26.53)

print("Dados do primeiro livro: ")
print(PrimeiroLivro.exibir_dados())
print("\n")
print("Dados do segundo livro: ")
print(SegundoLivro.exibir_dados())