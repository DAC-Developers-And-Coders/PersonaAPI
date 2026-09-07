from pydantic import BaseModel

class Arcana(BaseModel):
    id: int
    nome: str
    descricao: str