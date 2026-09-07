from pydantic import BaseModel

class Elemento(BaseModel):
    id: int
    nome: str