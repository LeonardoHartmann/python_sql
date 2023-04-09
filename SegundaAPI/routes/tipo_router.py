from typing import Any, List, Optional
from fastapi import (
    APIRouter,
    HTTPException,
    status,
    Response,
    Path,
    Depends
)
from fastapi.encoders import jsonable_encoder
from models.tipo_model import Tipo
from config import fake_db
from core.database import connection

router = APIRouter()


@router.get('/tipos',
            description="Retorna todos os usuarios",
            summary="Todos os usuarios",
            response_model=List[Tipo],
            response_description="Deu certo")
async def get_tipos():
    cursor = connection.cursor(dictionary=True)

    cursor.execute("select * from tipo")
    results = cursor.fetchall()
    
    cursor.close()
    connection.close()
    return results
