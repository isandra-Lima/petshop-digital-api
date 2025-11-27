from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class DonoBase(BaseModel):
    nome: str
    telefone: str

class DonoCreate(DonoBase):
    pass 

# 2. Pet
class PetBase(BaseModel):
    nome: str
    tipo: str  
    porte: str 
    dono_id: int 

class PetCreate(PetBase):
    pass 


class HistoricoServicoBase(BaseModel):
  
    preco_final: float
    data_aplicacao: Optional[datetime] = None
    
   
    class Config:
        from_attributes = True





class Dono(DonoBase):
    id: int
    
    class Config:
        from_attributes = True


class Pet(PetBase):
    id: int
 
    class Config:
        from_attributes = True


class Servico(BaseModel):
    id: int
    nome: str
    preco_base: float
    
    class Config:
        from_attributes = True