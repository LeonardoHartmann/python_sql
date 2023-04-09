from fastapi import FastAPI

from routes import (
    curso_router, 
    usuario_router,
    tipo_router)

API_V1_STR: str = '/api/v1'

app = FastAPI(
    title="Api de cursos",
    version="1.0.1",
    description="Uma API especial para pessoas especiais"
)
app.include_router(curso_router.router, tags=['cursos'], 
                   prefix=API_V1_STR)
app.include_router(usuario_router.router, tags=['Usuarios'], 
                   prefix=API_V1_STR)
app.include_router(tipo_router.router, prefix=API_V1_STR, tags=['Tipos'])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000,
                log_level="info", reload=True)
