from datetime import datetime
from pydantic import BaseModel, StrictStr # validação de dados 
from uuid import UUID

class Roteiro(BaseModel):
    id: UUID
    viagem_id: UUID
    dia: datetime
    lugar: StrictStr
    atividade: StrictStr
    create_at: datetime
    updated_at: datetime
    deleted_at: datetime
