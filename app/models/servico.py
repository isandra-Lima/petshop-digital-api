class Servico:
    def __init__(self, id: int, nome : str, preco: float):
        self.id = id
        self.nome = nome
        self.preco = preco
        
    def __repr__(self):
        return f"Servico(id={self.id}, nome='{self.nome}, preco={self.preco})"