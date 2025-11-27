from sqlalchemy import Column, Interger, String
from app.database import Base


class Tutor(Base):
    __tablename__ = "tutores"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    telefone = Column(String, nullable=False)