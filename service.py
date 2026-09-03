import json
import os

ARQUIVO = "usuarios.json"


def carregar_usuarios():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_usuarios(usuarios):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(usuarios, arquivo, ensure_ascii=False, indent=4)


def criar_usuario(usuario):
    usuarios = carregar_usuarios()
    novo_id = max((u["id"] for u in usuarios), default=0) + 1

    novo_usuario = {
        "id": novo_id,
        "nome": usuario["nome"],
        "email": usuario["email"],
        "idade": usuario.get("idade")
    }

    usuarios.append(novo_usuario)
    salvar_usuarios(usuarios)
    return novo_usuario


def listar_usuarios():
    return carregar_usuarios()


def buscar_usuario(usuario_id):
    usuarios = carregar_usuarios()
    for usuario in usuarios:
        if usuario["id"] == usuario_id:
            return usuario
    return None


def atualizar_usuario(usuario_id, dados):
    usuarios = carregar_usuarios()

    for usuario in usuarios:
        if usuario["id"] == usuario_id:
            usuario["nome"] = dados.get("nome", usuario["nome"])
            usuario["email"] = dados.get("email", usuario["email"])
            usuario["idade"] = dados.get("idade", usuario["idade"])
            salvar_usuarios(usuarios)
            return usuario

    return None


def excluir_usuario(usuario_id):
    usuarios = carregar_usuarios()

    for usuario in usuarios:
        if usuario["id"] == usuario_id:
            usuarios.remove(usuario)
            salvar_usuarios(usuarios)
            return True

    return False
