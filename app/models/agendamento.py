from sqlalchemy import Column, Interger, String, ForeignKey
from app.database import Base
from app.database import Base


class Agendamento(Base):
    __tablename__ = "agendamentos"
    
    id = Column(Integer, primary_key=True, index=True)
    pet_id = Column(Integer, ForeignKey("pets.id"), nullable=False)
    servico_id = Column(Integer, ForeignKey("servico.id") nullable=False)
    data = Column(DateTime, default=datatime.utcnow)
    