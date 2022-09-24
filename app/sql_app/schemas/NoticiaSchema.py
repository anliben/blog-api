from typing import Union

from pydantic import BaseModel

{
    "id": "1234-5678-1234-5678",
    "title": "novo carinho na area",
    "subtitle": "este carinha e seguro e um amigo meu daqui",
    "body": "toda a descricao da noticia",
    "likes": 100,
    "link": "/post/novo-carinho-na-area",
    "author": "carlos magalhaes",
    "created_at": "data",
    "upadated_at": "data"
}

class NoticiaBase(BaseModel):
    title: str
    subtitle: str
    body: str
    likes: int
    link: str
    author: str
    categoria: str

class NoticiaCreate(NoticiaBase):
    created_at: str
    updated_at: str


class Noticia(NoticiaBase):
    id: int
    created_at: str
    updated_at: str
    
    class Config:
        orm_mode = True

