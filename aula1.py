class Livraria:
    def __init__(self):
        self.estoque = {}

    def adicionar_livro(self, titulo, quantidade):
        if titulo in self.estoque:
            self.estoque[titulo] += quantidade
        else:
            self.estoque[titulo] = quantidade

    def remover_livro(self, titulo, quantidade):
        if titulo in self.estoque:
            if self.estoque[titulo] >= quantidade:
                self.estoque[titulo] -= quantidade
                if self.estoque[titulo] == 0:
                    del self.estoque[titulo]
                return True
            else:
                print(f"Não há estoque suficiente para remover {quantidade} cópias de '{titulo}'.")
        else:
            print(f"O livro '{titulo}' não está no estoque.")
        return False
    print("Alou")

    def listar_livros(self):
        if self.estoque:
            print("Livros disponíveis:")
            for titulo, quantidade in self.estoque.items():
                print(f"{titulo}: {quantidade} cópias")
        else:
            print("Bosta")