from fastapi import FastAPI
from app.database import engine
from app.models.models import Base
from app.controllers.petshop_controller import router

Base.metadata.create_all(bind=engine)
app = FastAPI(title="API Petshop - Projeto POO")

app.include_router(router, prefix="/router")


