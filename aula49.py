class Livro:
    def __init__(self, titular, autor, disponivel=True):
        self.titular = titular
        self.autor = autor
        self.disponivel = disponivel

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return 'Livro emprestado com sucesso.'
        return 'Livro indisponível.'

    def devolver(self):
        if self.disponivel:
            return 'Livro já está disponivel.'
        self.disponivel = True
        return 'Livro devolvido com sucesso.'

    def status(self):
        return f'Livro: {self.titular}\nAutor: {self.autor}\nDisponível: {self.disponivel}'
    
p1 = Livro('Harry Potter', 'J.K Rowling')
print(p1.emprestar())
print()
print(p1.status())
print()
print(p1.devolver())
print()
print(p1.status())