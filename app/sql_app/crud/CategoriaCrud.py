from sqlalchemy.orm import Session

from app.sql_app.models import CategoriaModel
from app.sql_app.schemas import CategoriaSchema


def get_categoria(db: Session, categoria_title: int):
    return db.query(CategoriaModel.Categoria).filter(CategoriaModel.Categoria.title == categoria_title).first()


def get_categorias(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CategoriaModel.Categoria).offset(skip).limit(limit).all()

def create_categoria(db: Session, categoria: CategoriaSchema.CategoriaCreate):
    db_categoria = CategoriaModel.Categoria(**categoria.dict())
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

def delete_categoria(db: Session, categoria_id: int):
    return db.query(CategoriaModel.Categoria).filter(CategoriaModel.Categoria.id == categoria_id).delete()

def update_categoria(db: Session, categoria_title: str, categoria: CategoriaSchema.CategoriaCreate):
    db_categoria = db.query(CategoriaModel.Categoria).filter(CategoriaModel.Categoria.title == categoria_title).first()
    db_categoria.title = categoria.title
    db_categoria.description = categoria.description
    db.commit()
    db.refresh(db_categoria)
    return db_categoria