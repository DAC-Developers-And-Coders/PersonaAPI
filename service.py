from Model.Arcana import Arcana
from Model.Elemento import Elemento
from Model.Database import Database as Db
from Model.Persona import Persona, PersonaGet
from pydantic import TypeAdapter, ValidationError

database = Db()
database.initialize_database()

def criar_persona(persona):
    nova_persona = persona.model_dump()
    persona_id = database.insert_data('Persona', nova_persona)

    return Persona(id=persona_id, **nova_persona)

def listar_personas():
    resultado = database.get_all_data('Persona')
    return [PersonaGet(**persona) for persona in resultado]

def listar_elementos():
    resultado = database.get_all_data('Elemento')
    return [Elemento(**elemento) for elemento in resultado]

def listar_arcanas():
    resultado = database.get_all_data('Arcana')
    return [Arcana(**arcana) for arcana in resultado]

def buscar_dado(nome_tabela, dado_id):
    resultado = database.get_specific_data(nome_tabela, 'id', dado_id)

    if not resultado:
        return None

    if nome_tabela == 'Persona':
        return PersonaGet(**resultado)
    elif nome_tabela == 'Elemento':
        return Elemento(**resultado)
    elif nome_tabela == 'Arcana':
        return Arcana(**resultado)
    return None

def atualizar_persona(persona_id, persona):
    persona_atual = buscar_dado('Persona', persona_id)

    if not persona_atual:
        return None

    persona_atualizada = persona.model_dump()

    database.update_data('Persona', persona_atualizada, persona_id)

    return Persona(id=persona_id, **persona_atualizada)

def excluir_persona(persona_id):
    if not verificar_dado_especifico('Persona', persona_id):
        return False

    database.delete_data('Persona', persona_id)
    return True

def atualizar_atributo(persona_id, atributo, valor):
    if not verificar_dado_especifico('Persona', persona_id):
        return None

    if atributo not in Persona.model_fields:
        return "Erro de atributo"
    elif atributo == 'id':
        return "Erro de acesso"

    campo = Persona.model_fields[atributo]

    try:
        valor_validado = TypeAdapter(campo.annotation).validate_python(valor, strict=True)
    except ValidationError:
        return "Erro de tipo"

    database.update_specific_attribute('Persona', atributo, valor_validado, persona_id)

    return buscar_dado('Persona', persona_id)

def verificar_tabela(table_name):
    resultado = database.verify_table_data(table_name)
    return bool(resultado)

def verificar_dado_especifico(table_name, element_id):
    resultado = database.verify_specific_value(table_name, element_id)
    return bool(resultado)