from datetime import date
from typing import Optional
from pydantic import BaseModel


class LancamentoModel(BaseModel):
    id: Optional[int]
    tipo: int
    data: date
    observacao: str
    valor: float
