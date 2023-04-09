from typing import Any, List, Optional
from fastapi import (
    APIRouter,
    HTTPException,
    status,
    Response,
    Path,
    Depends
)
from models.usuario_model import Usuario, usuarios
from config import fake_db

router = APIRouter()


@router.get('/usuarios',
            description="Retorna todos os usuarios",
            summary="Todos os usuarios",
            response_model=List[Usuario],
            response_description="Deu certo")
async def get_usuarios(db: Any = Depends(fake_db)):
    return usuarios


@router.get('/usuario/{usuario_id}',
            response_model=Usuario)
async def get_usuario(usuario_id: int = Path(default=None,
                                             title="Id do usuario",
                                             description="Deve ser entre 1 e 2",
                                             gt=0, lt=10),
                      db: Any = Depends(fake_db)):
    try:
        usuario = usuarios[usuario_id]
        return usuario
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario nao encontrado"
        )


@router.post('/usuario', status_code=status.HTTP_201_CREATED,
             response_model=Usuario)
async def post_usuario(usuario: Usuario, db: Any = Depends(fake_db)):
    next_id: int = len(usuarios) + 1
    usuario.id = next_id
    usuarios.append(usuario)
    return usuario


@router.put('/usuario/{usuario_id}', status_code=status.HTTP_202_ACCEPTED)
async def put_usuario(usuario_id: int, usuario: Optional[Usuario], db: Any = Depends(fake_db)):
    if usuario_id in usuarios:
        usuarios[usuario_id] = usuario
        return usuario
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Usuario nao encontrado: {usuario_id}")


@router.delete('/usuario/{usuario_id}')
async def delete_usuario(usuario_id: int, db: Any = Depends(fake_db)):
    if usuario_id in usuarios:
        del usuarios[usuario_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Usuario nao encontrado: {usuario_id}")
