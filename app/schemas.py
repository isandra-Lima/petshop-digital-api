from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class TutorCreate(BaseModel):
    nome: str
    telefone: int

class Tutor(BaseModel):
    id: int
    nome: str
    telefone: str

    class Config:
        orm_mode = True


class PetCreate(BaseModel):
    nome: str
    especie: str
    porte: str
    

class Pet(BaseModel):
    id: int
    nome: str
    especie: str
    porte: str

    class Config:
        orm_mode = True


class ServicoCreate(BaseModel):
    nome: str
    preco_base: float

class Servico(BaseModel):
    id: int
    nome: str
    preco_base: float

    class Config:
        orm_mode = True


class HistoricoDetalhe(BaseModel):
    pet: str
    servico: str
    preco: float
    data: datetime

class HistoricoResponse(BaseModel):
    tutor_id: int
    total_gasto: float
    servicos_detalhes: List[HistoricoDetalhe]
