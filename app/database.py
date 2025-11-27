from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base 
from typing import Generator
from typing import Generator


DATABASE_URL = "sqlite:///./petshop.db" 


    DATABASE_URL, 
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
)


Base = declarative_base()


def get_db() -> Generator:
    """Função que abre e fecha a sessão do banco de dados para cada requisição."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()