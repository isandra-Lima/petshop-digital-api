from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List 
import uvicorn


from . import models, database 
from .schemas import DonoCreate, Dono, PetCreate, Pet, HistoricoServico


models.Base.metadata.create_all(bind=database.engine)


app = FastAPI(
    title="🐾 PetShop Digital API",
    description="API para gerenciamento de pets, donos e serviços."
)



@app.post("/donos/", response_model=Dono, status_code=status.HTTP_201_CREATED, tags=["Donos"])
def create_dono(dono: DonoCreate, db: Session = Depends(database.get_db)):
    """Cadastra um novo dono (Tutor) no banco de dados."""
    
  
    db_dono = models.Dono(**dono.dict())
    
    db.add(db_dono)
    db.commit()
    db.refresh(db_dono)
    
    return db_dono

@app.post("/pets/", response_model=Pet, status_code=status.HTTP_201_CREATED, tags=["Pets"])
def create_pet(pet: PetCreate, db: Session = Depends(database.get_db)):
    """Cadastra um pet e o associa a um dono (Tutor) existente."""
    
   
    dono = db.query(models.Dono).filter(models.Dono.id == pet.dono_id).first()
    if not dono:
        raise HTTPException(status_code=404, detail=f"Dono com id {pet.dono_id} não encontrado.")

    
    db_pet = models.Pet(**pet.dict())
    
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    
    return db_pet



@app.get("/pets/", response_model=List[Pet], tags=["Pets"])
def read_pets(db: Session = Depends(database.get_db)):
    """Lista todos os pets cadastrados no banco de dados."""
    pets = db.query(models.Pet).all()
    return pets

@app.get("/servicos/historico/{dono_id}", tags=["Serviços"])
def read_historico(dono_id: int, db: Session = Depends(database.get_db)):
    """Consulta o histórico de serviços e a soma total para um dono específico."""
    
    historico_query = (
        db.query(models.HistoricoServico, models.Pet, models.Servico)
        .join(models.Pet)
        .join(models.Servico)
        .filter(models.Pet.dono_id == dono_id)
        .all()
    )

    if not historico_query:
        
        return {"dono_id": dono_id, "total_gasto": 0.0, "servicos_detalhes": []}

    total_gasto = sum(item[0].preco_final for item in historico_query)

    detalhes = [
        {
            "pet_nome": pet.nome,
            "servico_nome": servico.nome,
            "preco": registro.preco_final,
            "data": registro.data_aplicacao.strftime("%Y-%m-%d %H:%M:%S") if registro.data_aplicacao else None
        }
        for registro, pet, servico in historico_query
    ]
    
    return {
        "dono_id": dono_id,
        "total_gasto": round(total_gasto, 2),
        "servicos_detalhes": detalhes
    }
    


@app.post("/servicos/{pet_id}/{tipo}", tags=["Serviços"])
def aplicar_servico(pet_id: int, tipo: str, db: Session = Depends(database.get_db)):
    """
    Aplica um serviço a um pet. Requer a lógica de POO para calcular o preço final.
    Você preparou o banco (HistoricoServico) para receber este registro.
    """
   
    pet_db = db.query(models.Pet).filter(models.Pet.id == pet_id).first()
    servico_db = db.query(models.Servico).filter(models.Servico.nome == tipo).first()
    
    if not pet_db or not servico_db:
        raise HTTPException(status_code=404, detail="Pet ou Serviço não encontrado.")
    
    
    
    
    preco_final_calculado = servico_db.preco_base 
    
    
    novo_registro = models.HistoricoServico(
        pet_id=pet_id,
        servico_id=servico_db.id,
        preco_final=preco_final_calculado 
    )
    
    db.add(novo_registro)
    db.commit()
    db.refresh(novo_registro)
    
    return {"message": f"Serviço '{tipo}' aplicado com sucesso!", "registro_id": novo_registro.id, "preco": preco_final_calculado}

# -------------------------------------------------------------------
if __name__ == "__main__":
    
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)