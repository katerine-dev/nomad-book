from datetime import datetime
from pydantic import BaseModel, StrictStr # validação de dados 
from uuid import UUID

class Usuario(BaseModel):
    id: UUID
    email: StrictStr
    nome: StrictStr
    senha: StrictStr
    create_at: datetime
    updated_at: datetime

