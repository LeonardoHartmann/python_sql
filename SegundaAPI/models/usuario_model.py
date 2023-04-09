from typing import Optional
from pydantic import BaseModel, validator


class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    login: str 
    senha: str

    @validator('nome')
    def validar_nome(cls, value: str):
        palavras = value.split(" ")
        if len(palavras) < 2:
            raise ValueError('Informe pelos menos 2 palavras oreiudo!')

        if value.islower():
            raise ValueError(
                'O bocó alguma coisa em maisculo voce digitar ter')

        return value

    @validator('login')
    def validar_login(cls, value: str):
        if (len(value) < 5):
            raise ValueError('Tem que ter 5 ou mais caracteres')

        return value

    @validator('senha')
    def validar_senha(cls, value: str):
        if (len(value) < 6):
            raise ValueError("O bobaião tem que ter pelo menos 6 caracteres")
        return value


usuarios = [
    Usuario(id=1, nome="Nome do usuario 1", login="aaaaaaaaaaaa", senha="1234567890"),
    Usuario(id=2, nome="Nome do usuario 2", login="aaaaaaaaaaaa", senha="1234567890"),
    Usuario(id=3, nome="Nome do usuario 3", login="aaaaaaaaaaaa", senha="1234567890"),
    Usuario(id=4, nome="Nome do usuario 4", login="aaaaaaaaaaaa", senha="1234567890"),
    Usuario(id=5, nome="Nome do usuario 5", login="aaaaaaaaaaaa", senha="1234567890"),
    Usuario(id=6, nome="Nome do usuario 6", login="aaaaaaaaaaaa", senha="1234567890"),
    Usuario(id=7, nome="Nome do usuario 7", login="aaaaaaaaaaaa", senha="1234567890"),
    Usuario(id=8, nome="Nome do usuario 8", login="aaaaaaaaaaaa", senha="1234567890"),
]
