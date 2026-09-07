from pydantic import BaseModel

class PersonaCreate(BaseModel):
    nome: str
    origem: str
    primeira_aparicao: str
    classe: str | None = None
    nivel_inicial: int
    arcana_id: int
    elemento_id: int

class Persona(PersonaCreate):
    id: int

class PersonaGet(BaseModel):
    id: int
    nome: str
    origem: str
    primeira_aparicao: str
    classe: str | None = None
    nivel_inicial: int
    nome_arcana: str
    nome_elemento: str