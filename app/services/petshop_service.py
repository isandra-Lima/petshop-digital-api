from abc import ABC, abstractmethod


class ServicoBase(ABC):
    def __init__(self, preco_base: float):
        self.preco_base = preco_base

    @abstractmethod
    def calcular_preco(self, especie: str, porte: str) -> float:
        raise NotImplementedError


class Banho(ServicoBase):
    def calcular_preco(self, especie: str, porte: str) -> float:
        especie = (especie or "").lower()
        porte = (porte or "").lower()
        ajuste = 0.0
        if especie == "cachorro":
            if porte == "pequeno":
                ajuste = 0.0
            elif porte == "medio":
                ajuste = 5.0
            else:
                ajuste = 10.0
        elif especie == "gato":
            ajuste = -2.0
        elif especie == "passaro":
            ajuste = -3.0
        return max(0.0, self.preco_base + ajuste)


class Tosa(ServicoBase):
    def calcular_preco(self, especie: str, porte: str) -> float:
        especie = (especie or "").lower()
        porte = (porte or "").lower()
        ajuste = 0.0
        if especie == "cachorro":
            if porte == "pequeno":
                ajuste = 5.0
            elif porte == "medio":
                ajuste = 10.0
            else:
                ajuste = 20.0
        else:
            ajuste = 0.0
        return max(0.0, self.preco_base + ajuste)


class Vacina(ServicoBase):
    def calcular_preco(self, especie: str, porte: str) -> float:
        
        return max(0.0, self.preco_base)


def criar_servico_obj(nome: str, preco_base: float) -> ServicoBase:
    key = (nome or "").strip().lower()
    if key == "banho":
        return Banho(preco_base)
    if key == "tosa":
        return Tosa(preco_base)
    if key == "vacina":
        return Vacina(preco_base)
    
    class Generic(ServicoBase):
        def calcular_preco(self, especie, porte):
            return self.preco_base
    return Generic(preco_base)
