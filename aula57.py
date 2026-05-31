class Biblioteca:
    def __init__(self, nome, colecao: list) -> None:
        self._nome = nome
        self._colecao = colecao

    @property
    def colecao(self):
        return self._colecao
    
    @colecao.setter
    def colecao(self, valor: list):
        self._colecao = valor


class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def inf_livro(self):
        return f"Titulo: {self.titulo}\nAutor: {self.autor}"
    
biblioteca = Biblioteca("Biblioteca Municipal", ["A Megera Domada", "William Shakespeare"])
livro = Livro("Recordações do escrivão Isaias Caminha", "Lima Barreto")
biblioteca.colecao = livro
print(livro.inf_livro())
print()