from fastapi import APIRouter, Depends
from app.schemas import PetSchemas
from app.services.pet_service import PetService
from app.database import get_db

router = APIRouter(prefix="/pets")
service = PetService()

@router.get("/")
def listar(db = Depends(get_db)):
    return service.listar(db)

@router.post("/")
def criar(dados: PetSchemas, db = Depends(get_db)):
    return service.criar(db, dados)