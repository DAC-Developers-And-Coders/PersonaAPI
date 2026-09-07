from Model.Persona import Persona, PersonaCreate
from typing import Any
import service

def criar_persona(persona: PersonaCreate):
    return service.criar_persona(persona)

def atualizar_persona(persona_id: int, persona: PersonaCreate):
    return service.atualizar_persona(persona_id, persona)

def listar_personas():
    return service.listar_personas()

def listar_elementos():
    return service.listar_elementos()

def listar_arcanas():
    return service.listar_arcanas()

def verificar_tabelas(table_name: str):
    return service.verificar_tabela(table_name)

def verificar_opcoes_personas():
    return {"Allow": "GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS"}

def verificar_opcoes_gerais():
    return {"Allow": "GET, HEAD, OPTIONS"}

def verificar_dado_especifico(nome_tabela: str, dado_id: int):
    return service.verificar_dado_especifico(nome_tabela, dado_id)

def buscar_dado(nome_tabela: str, persona_id: int):
    return service.buscar_dado(nome_tabela, persona_id)

def excluir_persona(persona_id: int):
    return service.excluir_persona(persona_id)

def atualizar_atributo(persona_id: int, attribute: str, valor: Any):
    resultado = service.atualizar_atributo(persona_id, attribute, valor)

    if resultado is None:
        return None
    elif resultado == "Erro de atributo":
        return 404
    elif resultado == "Erro de acesso":
        return 403
    elif resultado == "Erro de tipo":
        return 422
    return resultado