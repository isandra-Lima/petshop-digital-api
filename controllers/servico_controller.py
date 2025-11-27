from fastapi import APIRouter, Depends
from app.schemas import ServicoSchemas
from app.services.servico_service import ServicoService
from app.database import get_db

router = APIRouter(prefix="/servicos")
service = ServicoService()

@router.get("/")
def listar(db = Depends(get_db)):
    return service.listar(db)

@router.post("/")
def criar(dados: ServicoSchemas, db = Depends(get_db)):
    return service.criar(db, dados)