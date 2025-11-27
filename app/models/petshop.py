from sqlalchemy import Column, Interger, String, ForeignKey
from app.database import Base


class Petshop(Base):
    __tablename__ = "petshops"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    endereco = Column(String, nullable=False)
    