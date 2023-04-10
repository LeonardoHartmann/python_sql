from fastapi import APIRouter, status, HTTPException, Response
from typing import List
from models.lancamento_model import LancamentoModel
from core.database import connection #database seria a conexao do banco de dados


router = APIRouter()

@router.get('/', response_model=List[LancamentoModel])
async def get_lancamentos():
    cursor = connection.cursor(dictionary=True)
    cursor.execute("select * from lancamento")
    results = cursor.fetchall()

    cursor.close()
    return results


@router.get('/{lancamento_id}', response_model=LancamentoModel)
async def get_lancamento(lancamento_id: int):
    cursor = connection.cursor(dictionary=True)
    cursor.execute("select * from lancamento where id = %s", [lancamento_id])
    result = cursor.fetchone()

    cursor.close()
    # connection.close()
    return result


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=LancamentoModel)
async def post_lancamento(lancamento: LancamentoModel):
    #"lancamento" seria uma constante que faz desmembramento dos dados dentro de LancamentoModel, o quebrando em varios dados para que a pesquisa em sql seja feita
    
    sql = "insert into lancamento (tipo, data, observacao, valor) values (%s, %s, %s, %s)"
    valores = [lancamento.tipo, lancamento.data, lancamento.observacao, lancamento.valor]

    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql, valores)
    connection.commit()

    last_id = cursor.lastrowid
    cursor.execute("select * from lancamento where id = %s", [last_id])
    result = cursor.fetchone()

    cursor.close()
    # connection.close()
    return result


@router.put('/{lancamento_id}', status_code=status.HTTP_202_ACCEPTED, response_model=LancamentoModel)
async def put_lancamento(lancamento_id: int, lancamento: LancamentoModel):
    
    cursor = connection.cursor(dictionary=True)
    cursor.execute("select * from lancamento where id = %s", [lancamento_id])
    result = cursor.fetchone()
    
    if result:
        sql = "update lancamento set tipo = %s, data = %s, observacao = %s, valor = %s where id = %s"
        valores = [lancamento.tipo, lancamento.data, lancamento.observacao, lancamento.valor, lancamento_id]
        cursor.execute(sql, valores)
        connection.commit()

        cursor.execute("select * from lancamento where id = %s", [lancamento_id])
        result = cursor.fetchone()

        cursor.close()
        # connection.close()
        return result
    else:
        raise HTTPException(detail="Lancamento nao encontrado", 
                            status_code=status.HTTP_404_NOT_FOUND)


@router.delete('/{lancamento_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_lancamento(lancamento_id: int):
    cursor = connection.cursor(dictionary=True)
    cursor.execute("select * from lancamento where id = %s", [lancamento_id])
    result = cursor.fetchone()
    if result:
        sql = 'delete from lancamento where id = %s'
        cursor.execute(sql, [lancamento_id])
        connection.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(detail="Lancamento nao encontrado",
                            status_code=status.HTTP_404_NOT_FOUND)
