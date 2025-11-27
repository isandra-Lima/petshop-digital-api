from sqlalchemy import Column, Interger, String, ForeignKey
from app.database import Base


class Pet(Base):
    __tablename__ = "pets"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    especie = Column(String, nullable=False)
    idade = Column(String, nullable=False)
    
    tutor_id = Column(Integer, ForeignKey("tutores.id"), nullable=False)