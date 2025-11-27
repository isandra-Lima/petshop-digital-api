from app.models import Pet, Tutor

class PetService:
    
    def listar(self, db):
        return db.query(Pet).all()
    def criar(self, db, dados): 
        tutor = db.query(Tutor).filter(Tutor.id == dados.tutor.id).first()
        if not tutor:
            raise Exception("Tutor não encontrado.")
        
        pet = Pet (
            nome=dados.nome,
            especie=dados.especie,
            tutor_id=dados.tutor_id
        )
        db.add(pet)
        db.Commit()
        db.refresh(pet)
        return pet
        