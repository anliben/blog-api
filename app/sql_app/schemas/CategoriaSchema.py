from typing import Union

from pydantic import BaseModel
{
    "id": "1234-5678-1234-5678",
    "title": "novo carinho na area",
    "subtitle": "este carinha e seguro e um amigo meu daqui",
}

class CategoriaBase(BaseModel):
    title: str
    subtitle: str

class CategoriaCreate(CategoriaBase):
    pass

class Categoria(CategoriaBase):
    id: int

    class Config:
        orm_mode = True

