from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base 


class Dono(Base):
    __tablename__ = 'donos'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    telefone = Column(String)

   
    pets = relationship("Pet", back_populates="dono")


class Pet(Base):
    __tablename__ = 'pets'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    tipo = Column(String)  
    porte = Column(String)
   
    dono_id = Column(Integer, ForeignKey('donos.id'))


    dono = relationship("Dono", back_populates="pets")
    historico = relationship("HistoricoServico", back_populates="pet")
    

class Servico(Base):
    """Mapeia a tabela 'servicos'."""
    __tablename__ = 'servicos'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True) # Banho, Tosa, Vacina
    preco_base = Column(Float)


    __tablename__ = 'historico_servicos'

    id = Column(Integer, primary_key=True, index=True)
    
    
    pet_id = Column(Integer, ForeignKey('pets.id'))
    servico_id = Column(Integer, ForeignKey('servicos.id'))
    
    preco_final = Column(Float)
    data_aplicacao = Column(DateTime, default=datetime.utcnow)

    
    pet = relationship("Pet", back_populates="historico")
    servico = relationship("Servico")