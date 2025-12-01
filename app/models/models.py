from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class Tutor(Base):
    __tablename__ = 'Tutors'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    telefone = Column(String)

    pets = relationship("Pet", back_populates="tutor")


class Pet(Base):
    __tablename__ = 'pets'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    especie = Column(String)
    porte = Column(String)
    tutor_id = Column(Integer, ForeignKey("Tutors.id"))

    tutor = relationship("Tutor", back_populates="pets")
    historico = relationship("HistoricoServico", back_populates="pet")


class Servico(Base):
    __tablename__ = 'servicos'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True)  
    preco_base = Column(Float)


    historico = relationship("HistoricoServico", back_populates="servico")


class HistoricoServico(Base):
    __tablename__ = 'historico_servicos'

    id = Column(Integer, primary_key=True, index=True)
    pet_id = Column(Integer, ForeignKey('pets.id'))
    servico_id = Column(Integer, ForeignKey('servicos.id'))

    preco_final = Column(Float)
    data_aplicacao = Column(DateTime, default=datetime.utcnow)

    pet = relationship("Pet", back_populates="historico")
    servico = relationship("Servico", back_populates="historico")
