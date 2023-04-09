from fastapi import FastAPI, HTTPException, status


app = FastAPI(
    title="API para acessar a api",
    version="1.2.3",
    description="Esta api é usada para acessar alguma coisa"
)


@app.get('/msg',
         description="Escreve uma mensagem de Ola",
         name="Mensagem de Ola",
         response_description="Deu tudo certo")
async def mensagem():
    try:
        return {"msg": "Ola Mundo 3!"}
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Erro nao encontrado")


@app.get('/somar/{n1}/{n2}')
async def somar(n1: int, n2: int):
    return {"soma": f"Soma: {n1 + n2}"}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000,
                log_level="info", reload=True)
