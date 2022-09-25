from typing import List
from fastapi import APIRouter, Depends, HTTPException


from ..dependencies import get_token_header
from ..sql_app.crud import NoticiaCrud
from ..sql_app.schemas import NoticiaSchema

from app.sql_app.database import SessionLocal, engine
from app.sql_app.models import NoticiaModel

from sqlalchemy.orm import Session

NoticiaModel.Base.metadata.create_all(bind=engine)


router = APIRouter(
    prefix="/noticia",
    tags=["noticias"],
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

@router.get("/", response_model=List[NoticiaSchema.Noticia])
async def read_noticiais():
    return NoticiaCrud.get_noticias()

@router.post("/", response_model=NoticiaSchema.Noticia)
async def create_noticia(noticia: NoticiaSchema.NoticiaCreate, db: Session = Depends(get_db)):
    return NoticiaCrud.create_noticia(db, noticia)

@router.get("/{noticia_id}", response_model=NoticiaSchema.Noticia)
async def read_noticia_by_id(noticia_id: int, db: Session = Depends(get_db)):
    return NoticiaCrud.get_noticia(db, noticia_id)

@router.get("/categoria/{categoria}", response_model=NoticiaSchema.Noticia)
async def read_noticia_by_categoria(categoria: str,  db: Session = Depends(get_db)):
    return NoticiaCrud.get_noticia_by_categoria(db, categoria)

@router.delete("/{noticia_id}", response_model=NoticiaSchema.Noticia)
async def delete_noticia(noticia_id: int, db: Session = Depends(get_db)):
    return NoticiaCrud.delete_noticia(db, noticia_id)

@router.get("/likes/{noticia_id}", response_model=NoticiaSchema.Noticia)	
async def read_likes_noticias(noticia_id: int,  db: Session = Depends(get_db)):
    return NoticiaCrud.get_likes_noticia(db, noticia_id)

