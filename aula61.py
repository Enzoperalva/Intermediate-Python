class Biblioteca:
    def __init__(self, nome):
        self._nome = nome
        self._colecao_livros = []

    def adicionar_livros(self, livro):
        if livro in self._colecao_livros:
            print('Esse livro já foi adicionado!')
            return
        
        self._colecao_livros.append(livro)
    
    def remover_livros(self, indice_livro):
        if not self._colecao_livros:
            print("Nenhum livro foi adicionado.")
            return
        try:
            self._colecao_livros.pop(indice_livro)
        except IndexError:
            print("Indice inválido!")

    def listar_livros(self):
        if not self._colecao_livros:
            print("Nenhum livro foi adicionado.")
            return
        for item in self._colecao_livros:
            print(f"{item.titulo} - {item.autor} - {item.quantidade_pags}")
    
    def quantidade_total_paginas(self):
        total = sum([
            p.quantidade_pags 
            for p in self._colecao_livros
        ])

        print("Total de páginas de todos os livros:", total)

    def verificar_livro(self, nome):
        for livro in self._colecao_livros:
            if livro.titulo == nome:
                print(f"O livro {nome} está na biblioteca!")
                return
        print(f"O livro {nome} não está na biblioteca!")


class Livro:
    def __init__(self, titulo, autor, quantidade_pags):
        self.titulo = titulo
        self.autor = autor
        self.quantidade_pags = quantidade_pags

biblioteca = Biblioteca("Biblioteca Machado")
livro1 = Livro("A Megera Domada", "William Shakespeare", 120)
livro2 = Livro("Hamlet", "William Shakespeare", 150)
biblioteca.adicionar_livros(livro1)
biblioteca.adicionar_livros(livro1)
biblioteca.adicionar_livros(livro2)
biblioteca.listar_livros()
biblioteca.quantidade_total_paginas()
biblioteca.verificar_livro("Hamlet")
biblioteca.remover_livros(1)
biblioteca.listar_livros()
biblioteca.verificar_livro("A Megera Domada")
biblioteca.verificar_livro("Hamlet")
biblioteca.quantidade_total_paginas()