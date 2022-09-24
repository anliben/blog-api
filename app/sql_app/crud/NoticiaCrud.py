from sqlalchemy.orm import Session

from app.sql_app.models import NoticiaModel
from app.sql_app.schemas import NoticiaSchema


def get_noticia(db: Session, noticia_id: int):
    return db.query(NoticiaModel.Noticia).filter(NoticiaModel.Noticia.id == noticia_id).first()


def get_noticia_by_categoria(db: Session, categoria: str):
    return db.query(NoticiaModel.Noticia).filter(NoticiaModel.Noticia.categoria == categoria).first()


def get_noticias(db: Session, skip: int = 0, limit: int = 100):
    return db.query(NoticiaModel.Noticia).offset(skip).limit(limit).all()

def create_noticia(db: Session, noticia: NoticiaSchema.NoticiaCreate):
    db_noticia = NoticiaModel.Noticia(**noticia.dict())
    db.add(db_noticia)
    db.commit()
    db.refresh(db_noticia)
    return db_noticia

def updated_noticia(db: Session, noticia: NoticiaSchema.NoticiaCreate):
    db_noticia = NoticiaModel.Noticia(**noticia.dict())
    db.add(db_noticia)
    db.commit()
    db.refresh(db_noticia)
    return db_noticia


def get_likes_noticia(db: Session, noticia_id: int):
    return db.query(NoticiaModel.Noticia.likes).filter(NoticiaModel.Noticia.id == noticia_id).first()


def delete_noticia(db: Session, noticia_id: int):
    return db.query(NoticiaModel.Noticia).filter(NoticiaModel.Noticia.id == noticia_id).delete()
