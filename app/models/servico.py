from sqlalchemy import Column, Interger, String, Float
from app.database import Base


class Servico(Base):
    __tablename__ = "servicos"
    
    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String, nullable=False)
    preco = Column(Float, nullable=False)
    