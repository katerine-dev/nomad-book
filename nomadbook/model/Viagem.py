from datetime import datetime
from pydantic import BaseModel, StrictStr # validação de dados 
from uuid import UUID

class Viagem(BaseModel):
    id: UUID
    titulo: StrictStr
    descricao: StrictStr
    create_at: datetime
    updated_at: datetime
    created_by: UUID