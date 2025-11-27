from app.models import Agendamento, Pet, Servico

class AgendamentoService:
    
    def listar(self, db):
        return db.query(Agendamento).all()
    
    def criar(self, db, dados):
        pet = db.query(Pet).filter(Pet.id == dados.pet_id).first()
        if not pet:
            raise Exception("Pet não existe!")
        
        servico = db.query(Servico).filter(Servico.id == dados.servico_id).first()
        if not servico:
            raise Exception("Serviço não existe!")
        
        #Evitar Conflito horário
        existe = db.query(Agendamento).filter(
            Agendamento.pet_id == dados.pet_id,
            Agendamento.data == dados.data
        ).first()
        
        if existe:
            raise Exception("Já existe agendamento nesse horário.")
        
        agendamento = Agendamento(
            pet_id=dados.pet_id,
            servico_id=dados.servico_id,
            data=dados.data
        )
        
        db.add(agendamento)
        db.Commit()
        db.refresh(agendamento)
        return agendamento
        