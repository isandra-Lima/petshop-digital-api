from fastapi import APIRouter, Depends, HTTPException, status, Body
from typing import List
from sqlalchemy.orm import Session
from app.services.petshop_service import criar_servico_obj

from app.models.models import (
    Tutor as TutorModel,
    Pet as PetModel,
    Servico as ServicoModel,
    HistoricoServico
)
from app.database import get_db
from app.schemas import (
    TutorCreate, Tutor,
    PetCreate, Pet,
    ServicoCreate, Servico,
    HistoricoResponse
)

router = APIRouter()



@router.post("/Tutor", response_model=Tutor, status_code=status.HTTP_201_CREATED, tags=["Tutores"])
def create_tutor(tutor: TutorCreate, db: Session = Depends(get_db)):
    db_tutor = TutorModel(**tutor.dict())
    db.add(db_tutor)
    db.commit()
    db.refresh(db_tutor)
    return db_tutor


@router.post("/Pets", response_model=Pet, status_code=status.HTTP_201_CREATED, tags=["Pets"])
def create_pet(tutor_id: int,pet: PetCreate = Body(...),db: Session = Depends(get_db)):
    tutor = db.query(TutorModel).filter(TutorModel.id == tutor_id).first()

    if not tutor:
        raise HTTPException(status_code=404, detail="Tutor não encontrado.")

    db_pet = PetModel(
        nome=pet.nome,
        especie=pet.especie,
        porte=pet.porte,
        tutor_id=tutor_id
    )

    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    return db_pet


@router.get("/pets/", response_model=List[Pet], tags=["Pets"])
def list_pets(db: Session = Depends(get_db)):
    return db.query(PetModel).all()


@router.get("/servicos/precos", tags=["Serviços"])
def tabela_precos():
    # espécies e portes disponíveis
    especies = ["cachorro", "gato", "passaro"]
    portes = ["pequeno", "medio", "grande"]

    
    servicos = {
        "banho": 20.0,
        "tosa": 25.0,
        "vacina": 50.0,
    }

    lista = []

    for nome_servico, preco_base in servicos.items():
        servico_obj = criar_servico_obj(nome_servico, preco_base)

        for especie in especies:
            for porte in portes:
                preco = servico_obj.calcular_preco(especie, porte)

                lista.append({
                    "servico": nome_servico.capitalize(),
                    "especie": especie.capitalize(),
                    "porte": porte.capitalize(),
                    "preco": preco
                })

    return lista

@router.post("/servicos", response_model=Servico, status_code=status.HTTP_201_CREATED, tags=["Serviços"])
def create_service(servico: ServicoCreate, db: Session = Depends(get_db)):
    existing = db.query(ServicoModel).filter(ServicoModel.nome == servico.nome).first()
    if existing:
        raise HTTPException( status_code=400, detail="Já existe um serviço cadastrado com esse nome.")
    
    db_servico = ServicoModel(**servico.dict())
    db.add(db_servico)
    db.commit()
    db.refresh(db_servico)

    return db_servico

@router.post("/Aplicar_servico", tags=["Serviços"]) 
def aplicar_servico(
    pet_nome: str = Body(...),
    servico_nome: str = Body(...),
    db: Session = Depends(get_db)
):

    pet = db.query(PetModel).filter(PetModel.nome == pet_nome).first()
    if not pet:
        raise HTTPException(status_code=404, detail="Pet não encontrado.")

    servico = db.query(ServicoModel).filter(ServicoModel.nome == servico_nome).first()
    if not servico:
        raise HTTPException(status_code=404, detail="Serviço não encontrado.")

    
    servico_obj = criar_servico_obj(servico.nome, servico.preco_base)
    preco_final = servico_obj.calcular_preco(pet.especie, pet.porte)
    registro = HistoricoServico(
        pet_id=pet.id,
        servico_id=servico.id,
        preco_final=preco_final
    )

    db.add(registro)
    db.commit()
    db.refresh(registro)

    return {
        "mensagem": "Serviço aplicado com sucesso.",
        "pet": pet.nome,
        "servico": servico.nome,
        "preco_final": preco_final
    }


@router.get("/Historico_servico", response_model=HistoricoResponse, tags=["Serviços"])
def historico_servicos(tutor_id: int, db: Session = Depends(get_db)):

    query = (
        db.query(HistoricoServico, PetModel, ServicoModel)
        .join(PetModel)
        .join(ServicoModel)
        .filter(PetModel.tutor_id == tutor_id)
        .all()
    )

    if not query:
        return {"tutor_id": tutor_id, "total_gasto": 0, "servicos_detalhes": []}

    total = sum(item[0].preco_final for item in query)

    detalhes = [
        {
            "pet": pet.nome,
            "servico": servico.nome,
            "preco": hist.preco_final,
            "data": hist.data_aplicacao
        }
        for hist, pet, servico in query
    ]

    return {"tutor_id": tutor_id, "total_gasto": total, "servicos_detalhes": detalhes}




