from typing import Optional
from pydantic import BaseModel, validator


class Curso(BaseModel):
    id: Optional[int] = None
    nome: str
    aulas: int  # mais de 15
    horas: int  # mais de 30

    @validator('nome')
    def validar_titulo(cls, value: str):
        palavras = value.split(" ")
        if len(palavras) < 2:
            raise ValueError('Informe pelos menos 2 palavras oreiudo!')

        if value.islower():
            raise ValueError(
                'O bocó alguma coisa em maisculo voce digitar ter')

        return value

    @validator('aulas')
    def validar_aulas(cls, value: int):  # maior que 15
        if (value < 15):
            raise ValueError('Tem que ter 15 ou mais aulas')

        return value

    @validator('horas')
    def validar_horas(cls, value: int):  # maior que 30
        if (value < 30):
            raise ValueError("O bobaião tem que ter pelo menos 30 horas")
        return value


cursos = [
    Curso(id=1, nome="Programacao 1 basica", aulas=40, horas=80),
    Curso(id=2, nome="Programacao 2 media", aulas=20, horas=40),
    Curso(id=3, nome="Programacao 3 avancada", aulas=15, horas=80),
    Curso(id=4, nome="Programacao 4 monster", aulas=25, horas=30),
    Curso(id=5, nome="Programacao 5 ultra", aulas=30, horas=333),
    Curso(id=6, nome="Manutencao de ar condicionado", aulas=100, horas=250),
    Curso(id=7, nome="Atualizacao de impressora", aulas=100, horas=250),
    Curso(id=8, nome="Algoritmos 1", aulas=100, horas=250),
]