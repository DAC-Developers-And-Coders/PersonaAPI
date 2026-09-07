from fastapi import APIRouter, HTTPException, Response
import controller as ctrl

router = APIRouter(prefix="/arcanas", tags=["Arcanas"])

@router.get("")
def listar_arcanas():
    return ctrl.listar_arcanas()

@router.head("")
def verificar_arcanas():
    resultado = ctrl.verificar_tabelas('Arcana')

    if not resultado:
        raise HTTPException(status_code=404, headers={"mensagem": "nenhuma arcana encontrada"})
    return Response(status_code=200, headers={"mensagem": "arcanas encontradas"})

@router.options("")
def verificar_opcoes():
    return Response(status_code=204, headers=ctrl.verificar_opcoes_gerais())

@router.head("/{arcana_id}")
def verificar_arcana_especifica(arcana_id: int):
    if not ctrl.verificar_dado_especifico('Arcana', arcana_id):
        raise HTTPException(status_code=404, headers={"mensagem": "arcana não encontrada"})
    return Response(status_code=200, headers={"mensagem": "arcana encontrada"})

@router.get("/{arcana_id}")
def buscar_arcana(arcana_id: int):
    arcana = ctrl.buscar_dado('Arcana', arcana_id)

    if not arcana:
        raise HTTPException(status_code=404, detail="Arcana não encontrada")
    return arcana