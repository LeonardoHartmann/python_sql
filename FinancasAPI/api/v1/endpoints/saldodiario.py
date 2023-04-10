from fastapi import APIRouter
from typing import List
from models.saldodiario_model import SaldoDiarioModel
from core.database import connection #database seria a conexao do banco de dados


router = APIRouter()

#lista todas as datas e todos os saldos 
@router.get('/saldos', response_model=List[SaldoDiarioModel])
async def get_saldos():
    cursor = connection.cursor(dictionary=True)
    cursor.execute("select * from saldodiario")
    results = cursor.fetchall()

    cursor.close()
    return results

#pesquisa por data
@router.get('/data/{data}', response_model=SaldoDiarioModel)
async def get_saldodata(data: str):
    cursor = connection.cursor(dictionary=True)
    cursor.execute("select * from saldodiario where data = %s", [data])
    result = cursor.fetchone()

    cursor.close()
    # connection.close()
    return result

#pesquisa por periodos
@router.get('/periodo', response_model=SaldoDiarioModel)
async def get_periodo(data_inicial: str, data_final: str):
    cursor = connection.cursor(dictionary=True)
    sql=("SELECT * FROM saldodiario WHERE data BETWEEN data AND data values (%s, %s)")
    valores = (data_inicial, data_final) 
    cursor.execute(sql, valores)
    result = cursor.fetchone()

    cursor.close()
    # connection.close()
    return result

