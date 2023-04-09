from typing import Any, List, Optional
from fastapi import (
    APIRouter,
    HTTPException,
    status,
    Response,
    Path,
    Depends
)
from models.curso_model import Curso, cursos
from config import fake_db

router = APIRouter()
"""
@router.get('/api/v1/cursos')
async def get_cursos():
    return {'info': "Todos os curso"}
"""


@router.get('/cursos',
         description="Retorna todos os cursos",
         summary="Todos os cursos",
         response_model=List[Curso],
         response_description="Deu certo")
async def get_cursos(db: Any = Depends(fake_db)):
    return cursos

@router.get('/curso/{curso_id}',
         response_model=Curso)
async def get_curso(curso_id: int = Path(default=None,
                                         title="Id do curso",
                                         description="Deve ser entre 1 e 2",
                                         gt=0, lt=10),
                    db: Any = Depends(fake_db)):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Curso nao encontrado"
        )


@router.post('/curso', status_code=status.HTTP_201_CREATED,
          response_model=Curso)
async def post_curso(curso: Curso, db: Any = Depends(fake_db)):
    next_id: int = len(cursos) + 1
    curso.id = next_id
    cursos.append(curso)
    return curso


@router.put('/curso/{curso_id}', status_code=status.HTTP_202_ACCEPTED)
async def put_curso(curso_id: int, curso: Optional[Curso], db: Any = Depends(fake_db)):
    if curso_id in cursos:
        cursos[curso_id] = curso
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Curso nao encontrado: {curso_id}")


@router.delete('/curso/{curso_id}')
async def delete_curso(curso_id: int, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        del cursos[curso_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Curso nao encontrado: {curso_id}")
