from app.models import Tutor
from app.database import get_db

class TutorService:
    
    def listar(self, db):
        return db.query(Tutor).all()
    
    def criar(self, db, dados):
        tutor = Tutor(nome=dados.nome, telefone=dados.telefone)
        db.add(Tutor)
        db.Commit()
        db.refresh(tutor)
        return tutor