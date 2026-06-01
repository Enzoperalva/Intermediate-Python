class Biblioteca:
    def __init__(self, nome) -> None:
        self._nome = nome
        self._colecao = []

    def adicionar_livro(self, livro):
        self._colecao.append(livro)
        return "Livro adicionado!"
    
    def listar_livros(self):
        for livro in self._colecao:
            print(livro.inf_livro())
            print("-" * 20)

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def inf_livro(self):
        return f"Titulo: {self.titulo}\nAutor: {self.autor}"

biblioteca = Biblioteca("Biblioteca Municipal")
livro1 = Livro("Recordações do escrivão Isaias Caminha", "Lima Barreto")
biblioteca.adicionar_livro(livro1)
biblioteca.listar_livros()
