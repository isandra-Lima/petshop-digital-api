class Tutor:
    def __init__(self, id: int, nome: str, telefone: str):
        self.id = id
        self.nome = nome
        self.telefone = telefone

    def __repr__(self):
        return f"Tutor(id={self.id}, nome='{self.nome}')"
