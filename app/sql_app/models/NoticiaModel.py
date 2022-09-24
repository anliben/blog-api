from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.sql_app.database import Base


class Noticia(Base):
    __tablename__ = "noticias"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    subtitle = Column(String, index=True)
    body = Column(String, index=True)
    likes = Column(Integer, index=True)
    link = Column(String, index=True)
    author = Column(String, index=True)
    categoria = Column(String, index=True)
    created_at = Column(String, index=True)
    updated_at = Column(String, index=True)
