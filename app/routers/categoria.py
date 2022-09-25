from typing import List
from fastapi import APIRouter, Depends, HTTPException


from ..dependencies import get_token_header
from ..sql_app.crud import CategoriaCrud
from ..sql_app.schemas import CategoriaSchema
from app.sql_app.models import CategoriaModel

from app.sql_app.database import SessionLocal, engine

from sqlalchemy.orm import Session

CategoriaModel.Base.metadata.create_all(bind=engine)


router = APIRouter(
    prefix="/categoria",
    tags=["categoria"],
    #dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=List[CategoriaSchema.Categoria])
async def read_categoria(db: Session = Depends(get_db)):
    return CategoriaCrud.get_categorias(db)

@router.get("/{categoria_title}", response_model=CategoriaSchema.Categoria)
async def read_categoria(categoria_title: str,  db: Session = Depends(get_db)):
    return CategoriaCrud.get_categoria(db, categoria_title)

@router.post("/", response_model=CategoriaSchema.Categoria)
async def post_categoria(categoria: CategoriaSchema.CategoriaCreate, db: Session = Depends(get_db)):
    return CategoriaCrud.create_categoria(db, categoria)

@router.delete("/{categoria_title}", response_model=CategoriaSchema.Categoria)
async def delete_categoria(categoria_title: str, db: Session = Depends(get_db)):
    return CategoriaCrud.delete_categoria(db, categoria_title)

@router.put("/{categoria_title}", response_model=CategoriaSchema.Categoria)
async def update_categoria(categoria_title: str, categoria: CategoriaSchema.CategoriaCreate, db: Session = Depends(get_db)):
    return CategoriaCrud.update_categoria(db, categoria_title, categoria)
