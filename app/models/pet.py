from tutor import Tutor

class Pet:
    def __init__(self, id: int, nome: str, especie: str, idade: int, tutor: Tutor):
        self.id = id
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.tutor = tutor

    def __repr__(self):
        return f"Pet(id={self.id}, nome='{self.nome}', tutor='{self.tutor.nome}')"
