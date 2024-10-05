from datetime import datetime
from pydantic import BaseModel, StrictStr # validação de dados 
from uuid import UUID

class usuario(BaseModel):
    id: UUID
    email: StrictStr
    nome: StrictStr
    senha: StrictStr
    create_at: datetime
    updated_at: datetime


class viagem(BaseModel):
    id: UUID
    titulo: StrictStr
    descricao: StrictStr
    create_at: datetime
    updated_at: datetime
    created_by: UUID

class roteiro(BaseModel):
    id: UUID
    viagem_id: UUID
    dia: datetime
    lugar: StrictStr
    atividade: StrictStr
    create_at: datetime
    updated_at: datetime
    deleted_at: datetime

