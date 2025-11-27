from fastapi import APIRouter, Depends
from app.schemas import TutorSchemas
from app.services.tutor_service import TutorService
from app.database import get_db

router = APIRouter(prefix="/tutores")
service = TutorService()

@router.get("/")
def listar(db = Depends(get_db)):
    return service.listar(db)

@router.post("/")
def criar(dados: TutorSchemas, db = Depends(get_db)):
    return service.criar(db, dados)