from typing import Optional
from pydantic import BaseModel


class TipoModel(BaseModel):
    id: Optional[int]
    descricao: str
    tipo: str
    