from fastapi import APIRouter, HTTPException, Body, Response
from Model.Persona import Persona, PersonaCreate, PersonaGet
import controller as ctrl
from typing import Any

router = APIRouter(prefix="/personas", tags=["Personas"])

@router.post("", response_model=Persona)
def criar_persona(persona: PersonaCreate):
    return ctrl.criar_persona(persona)

@router.put("/{persona_id}", response_model=Persona)
def atualizar_persona(persona_id: int, persona: PersonaCreate):
    resultado = ctrl.atualizar_persona(persona_id, persona)
    if not resultado:
        raise HTTPException(status_code=404, detail="Persona não encontrada")
    return resultado

@router.get("", response_model=list[PersonaGet])
def listar_personas():
    return ctrl.listar_personas()

@router.head("")
def verificar_personas():
    resultado = ctrl.verificar_tabelas('Persona')

    if not resultado:
        raise HTTPException(status_code=404, headers={"mensagem": "Nenhuma persona encontrada"})
    return Response(status_code=200, headers={"mensagem": "Personas encontradas"})

@router.options("")
def verificar_opcoes():
    return Response(status_code=204, headers=ctrl.verificar_opcoes_personas())

@router.head("/{persona_id}")
def verificar_persona_especifica(persona_id: int):
    if not ctrl.verificar_dado_especifico('Persona', persona_id):
        raise HTTPException(status_code=404, headers={"mensagem": "Persona não encontrada"})
    return Response(status_code=200, headers={"mensagem": "Persona encontrada"})

@router.get("/{persona_id}", response_model=PersonaGet)
def buscar_persona(persona_id: int):
    persona = ctrl.buscar_dado('Persona', persona_id)

    if not persona:
        raise HTTPException(status_code=404, detail="Persona não encontrada")
    return persona

@router.delete("/{persona_id}")
def excluir_persona(persona_id: int):
    resultado = ctrl.excluir_persona(persona_id)
    if not resultado:
        raise HTTPException(status_code=404, detail="Persona não encontrada")
    return Response(status_code=204, headers={"mensagem": "Persona excluída com sucesso"})

@router.patch("/{persona_id}/{attribute}")
def atualizar_atributo(persona_id: int, attribute: str, valor: Any = Body(...)):
    resultado = ctrl.atualizar_atributo(persona_id, attribute, valor)

    if resultado is None:
        raise HTTPException(status_code=404, detail="Persona não encontrada")
    elif resultado == 404:
        raise HTTPException(status_code=404, detail="Atributo não encontrado")
    elif resultado == 403:
        raise HTTPException(status_code=403, detail="Acesso negado")
    elif resultado == 422:
        raise HTTPException(status_code=422, detail="Tipo de dado inválido")
    return resultado