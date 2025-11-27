from fastapi import APIRouter, Depends
from app.schemas import AgendamentoSchemas
from app.services.agendamento_service import AgendamentoService
from app.database import get_db

router = APIRouter(prefix="/agendamentos")
service = AgendamentoService()

@router.get("/")
def lista(db = Depends(get_db)):
    return service.listar(db)

@router.post("/")
def criar(dados: AgendamentoSchemas, db = Depends(get_db)):
    return service.criar(db, dados)