import json
import os

from Model.Persona import Persona

ARQUIVO = "personas.json"


def carregar_personas():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_personas(personas):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(personas, arquivo, ensure_ascii=False, indent=4)


def criar_persona(persona):
    personas = carregar_personas()
    novo_id = max((u["id"] for u in personas), default=0) + 1

    novo_persona = {
        "id": novo_id,
        "nome": persona["nome"],
        "origem": persona["origem"],
        "arcanas": persona["arcanas"]
    }

    personas.append(novo_persona)
    salvar_personas(personas)
    return novo_persona


def listar_personas():
    return carregar_personas()


def buscar_persona(persona_id):
    personas = carregar_personas()
    for persona in personas:
        if persona["id"] == persona_id:
            return persona
    return None


def atualizar_persona(persona_id, dados):
    personas = carregar_personas()

    for persona in personas:
        if persona["id"] == persona_id:
            persona["nome"] = dados.get("nome", persona["nome"])
            persona["origem"] = dados.get("origem", persona["origem"])
            persona["arcanas"] = dados.get("arcanas", persona["arcanas"])
            salvar_personas(personas)
            return persona

    return None

def atualizar_atributo(persona_id, atributo, valor):
    personas = carregar_personas()

    for persona in personas:
        if persona["id"] == persona_id:

            if atributo not in persona:
                return "Erro de atributo"

            persona[atributo] = valor
            salvar_personas(personas)
            return persona

    return None


def excluir_persona(persona_id):
    personas = carregar_personas()

    for persona in personas:
        if persona["id"] == persona_id:
            personas.remove(persona)
            salvar_personas(personas)
            return True

    return False
