from typing import Optional
from pydantic import BaseModel, validator


class Tipo(BaseModel):
    id: Optional[int] = None
    descricao: str
    tipo: str 

    