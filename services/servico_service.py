from app.models import Servico

class ServicoService:
    def listar(self, db):
        return db.query(Servico).all()
    
    def criar(self, db, dados):
        servico= Servico(nome=dados.nome, preco=dados.preco)
        db.add(servico)
        db.Commit()
        db.refresh(servico)
        return servico
    
    