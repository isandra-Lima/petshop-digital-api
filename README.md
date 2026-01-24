# petshop-digital-api
# PetShop Digital API
API desenvolvida para gerenciamento de pets, donos e serviços (banho, tosa e vacinação) utilizando **FastAPI, POO e SQLAlchemy**.

Este projeto foi feito como atividade acadêmica para aplicar:
-  Programação Orientada a Objetos (Herança, Polimorfismo, Abstração)
-  Estruturas de decisão e repetição
- CRUD com API REST
- Banco de dados relacional
- Estruturas de dados (listas e dicionários)


## Tecnologias
- Python 3.10+
- FastAPI
- SQLAlchemy
- SQLite (pode ser trocado por outro banco)
- Uvicorn

---

## Requisitos do Projeto Atendidos
###  POO
- Classe base `Pet`
- Herança → `Cachorro`, `Gato`, `Pássaro`
- Abstração → classe `Servico`
- Polimorfismo → `Banho`, `Tosa`, `Vacina`

### Regras de Negócio
- Preço varia de acordo com porte e tipo do pet (decisão)
- Consulta de histórico e soma total de serviços (repetição)

### API REST
| Método | Rota | Descrição |
|--------|------|-----------|
| POST | `/pets` | Cadastra um pet |
| GET | `/pets` | Lista pets |
| POST | `/servicos/{pet_id}/{tipo}` | Aplica serviço |
| GET | `/servicos/historico/{dono_id}` | Consulta histórico e total |

---

## Como rodar o projeto
```bash
pip install fastapi uvicorn sqlalchemy
uvicorn main:app --reload
