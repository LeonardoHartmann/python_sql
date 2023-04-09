from typing import List
from fastapi import APIRouter, HTTPException, Response, status

from models.tipo_model import TipoModel
from core.database import connection


router = APIRouter()


@router.get('/', response_model=List[TipoModel])
async def get_tipos():
    cursor = connection.cursor(dictionary=True)
    cursor.execute("select * from tipo")
    results = cursor.fetchall()

    cursor.close()
    # connection.close()
    return results


@router.get('/{tipo_id}', response_model=TipoModel)
async def get_tipo(tipo_id: int):
    cursor = connection.cursor(dictionary=True)
    cursor.execute("select * from tipo where id = %s", [tipo_id])
    result = cursor.fetchone()

    cursor.close()
    # connection.close()
    return result


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=TipoModel)
async def post_tipo(tipo: TipoModel):
    sql = "insert into tipo (descricao, tipo) values (%s, %s)"
    valores = [tipo.descricao, tipo.tipo]

    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql, valores)
    connection.commit()

    last_id = cursor.lastrowid
    cursor.execute("select * from tipo where id = %s", [last_id])
    result = cursor.fetchone()

    cursor.close()
    # connection.close()
    return result


@router.put('/{tipo_id}', status_code=status.HTTP_202_ACCEPTED, response_model=TipoModel)
async def put_tipo(tipo_id: int, tipo: TipoModel):
    cursor = connection.cursor(dictionary=True)
    cursor.execute("select * from tipo where id = %s", [tipo_id])
    result = cursor.fetchone()
    if result:
        sql = "update tipo set descricao = %s, tipo = %s where id = %s"
        valores = [tipo.descricao, tipo.tipo, tipo_id]
        cursor.execute(sql, valores)
        connection.commit()

        cursor.execute("select * from tipo where id = %s", [tipo_id])
        result = cursor.fetchone()

        cursor.close()
        # connection.close()
        return result
    else:
        raise HTTPException(detail="Tipo nao encontrado", 
                            status_code=status.HTTP_404_NOT_FOUND)


@router.delete('/{tipo_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_tipo(tipo_id: int):
    cursor = connection.cursor(dictionary=True)
    cursor.execute("select * from tipo where id = %s", [tipo_id])
    result = cursor.fetchone()
    if result:
        sql = 'delete from tipo where id = %s'
        cursor.execute(sql, [tipo_id])
        connection.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(detail="Tipo nao encontrado",
                            status_code=status.HTTP_404_NOT_FOUND)
