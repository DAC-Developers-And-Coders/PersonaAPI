from fastapi import APIRouter, HTTPException, Response
import controller as ctrl

router = APIRouter(prefix="/elementos", tags=["Elementos"])

@router.get("")
def listar_elementos():
    return ctrl.listar_elementos()

@router.head("")
def verificar_elementos():
    resultado = ctrl.verificar_tabelas('Elemento')

    if not resultado:
        raise HTTPException(status_code=404, headers={"mensagem": "nenhum elemento encontrado"})
    return Response(status_code=200, headers={"mensagem": "elementos encontrados"})

@router.options("")
def verificar_opcoes():
    return Response(status_code=204, headers=ctrl.verificar_opcoes_gerais())

@router.head("/{elemento_id}")
def verificar_elemento_especifico(elemento_id: int):
    if not ctrl.verificar_dado_especifico('Elemento', elemento_id):
        raise HTTPException(status_code=404, headers={"mensagem": "elemento não encontrado"})
    return Response(status_code=200, headers={"mensagem": "elemento encontrado"})

@router.get("/{elemento_id}")
def buscar_elemento(elemento_id: int):
    elemento = ctrl.buscar_dado('Elemento', elemento_id)

    if not elemento:
        raise HTTPException(status_code=404, detail="Elemento não encontrado")
    return elemento