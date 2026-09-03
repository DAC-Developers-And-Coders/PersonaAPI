from email import header

from fastapi import APIRouter, HTTPException, Body, Response
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
        raise HTTPException(status_code=404, headers={"mensagem": "nenhuma persona encontrada"})
    return Response(status_code=200, headers={"mensagem": "personas encontradas"})

@router.options("")
def verificar_opcoes():
    return Response(status_code=204, headers={"Permite": "GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS"})

@router.head("/{persona_id}")
def verificar_persona_especifica(persona_id: int):
    if not service.verificar_persona_especifica(persona_id):
        raise HTTPException(status_code=404, headers={"mensagem": "persona não encontrada"})
    return Response(status_code=200, headers={"mensagem": "persona encontrada"})

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
