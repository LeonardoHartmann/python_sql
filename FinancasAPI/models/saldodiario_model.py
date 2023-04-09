from datetime import date
from pydantic import BaseModel


class SaldoDiarioModel(BaseModel):
    data: date
    saldo: float
