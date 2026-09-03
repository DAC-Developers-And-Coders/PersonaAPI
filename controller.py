from fastapi import APIRouter, HTTPException, Body
from typing import Any
import service

router = APIRouter(prefix="/personas", tags=["Personas"])

@router.post("")
def criar_persona(persona: dict):
    return service.criar_persona(persona)

@router.put("/{persona_id}")
def atualizar_persona(persona_id: int, persona: dict):
    resultado = service.atualizar_persona(persona_id, persona)
    if resultado is None:
        raise HTTPException(status_code=404, detail="Persona não encontrada")
    return resultado

@router.get("")
def listar_personas():
    return service.listar_personas()

@router.head("")
def verificar_personas():
    if not service.verificar_personas():
        raise HTTPException(status_code=404)

@router.head("/{persona_id}")
def verificar_persona_especifica(persona_id: int):
    if not service.verificar_persona_especifica(persona_id):
        raise HTTPException(status_code=404)

@router.get("/{persona_id}")
def buscar_persona(persona_id: int):
    persona = service.buscar_persona(persona_id)
    if persona is None:
        raise HTTPException(status_code=404, detail="Persona não encontrada")
    return persona

@router.delete("/{persona_id}")
def excluir_persona(persona_id: int):
    resultado = service.excluir_persona(persona_id)
    if not resultado:
        raise HTTPException(status_code=404, detail="Persona não encontrada")
    return {"mensagem": "Persona excluída com sucesso"}

@router.patch("/{persona_id}/{attribute}")
def atualizar_atributo(persona_id: int, attribute: str, valor: Any = Body(...)):
    resultado = service.atualizar_atributo(persona_id, attribute, valor)
    if resultado is None:
        raise HTTPException(status_code=404, detail="Persona não encontrada")
    elif resultado == "Erro de atributo":
        raise HTTPException(status_code=404, detail="Atributo não encontrado")
    return resultado
