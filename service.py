import sqlite3
from Model.Persona import Persona

BANCO = "personadb.db"

def conecta_banco():
    conn = sqlite3.connect(BANCO)
    conn.row_factory = sqlite3.Row
    return conn

def inicializa_banco():
    conn = conecta_banco()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS personas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            origem TEXT,
            arcanas TEXT
            )
        '''
    )
    conn.commit()
    conn.close()

inicializa_banco()

def criar_persona(persona):
    conn = conecta_banco()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO personas (nome, origem, arcanas) VALUES (?, ?, ?)",
        (persona["nome"], persona["origem"], persona["arcanas"])
    )
    conn.commit()

    novo_id = cursor.lastrowid
    conn.close()

    return {
        "id": novo_id,
        "nome": persona["nome"],
        "origem": persona["origem"],
        "arcanas": persona["arcanas"]
    }




def listar_personas():
    conn = conecta_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM personas")
    linhas = conn.fetchall()
    conn.close()

    return[dict(linha) for linha in linhas]

def verificar_personas():
    conn = conecta_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM personas LIMIT 1 ")
    resultado = cursor.fetchone()
    conn.close()

    return bool(resultado)

def buscar_persona(persona_id):
    conn = conecta_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM personas WHERE id = ?", (persona_id,))
    linha = cursor.fetchone()
    conn.close

    return dict(linha) if linha else None
    
def verificar_persona_especifica(persona_id):
    return buscar_persona(persona_id) is not None

def excluir_persona(persona_id):
    if not verificar_persona_especifica(persona_id):
        return False

    conn = conecta_banco()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM personas WHERE id = ?", (persona_id,))
    conn.commit()
    conn.close
    return True

def atualizar_persona(persona_id, dados):
    persona_atual = buscar_persona(persona_id)
    if not persona_atual:
        return None
    
    nome = dados.get("nome", persona_atual["nome"])
    origem = dados.get("origem", persona_atual["origem"])
    arcanas  = dados.get("arcanas", persona_atual["arcanas "])

    conn = conecta_banco()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE personas SET nome = ?, origem = ?, arcanas = ? WHERE id = ?",
        (nome, origem, arcanas, persona_id)
    )

    conn.commit()
    conn.close()
    
    return {"id": persona_id, "nome": nome, "origem": origem, "arcanas": arcanas}



def atualizar_atributo(persona_id, atributo,  dados):
    atributos_permitidos = ["nome", "origem", "arcanas"]
    if atributo not in atributos_permitidos:
        return "Erro de atributo"

    persona_atual = buscar_persona(persona_id)
    if not persona_atual:
        return None
    
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(f"UPDATE personas SET {atributo} = ? WHERE id = ?", (valor, persona_id))
    conn.commit()
    conn.close()

    persona_atual[atributo] = valor
    return persona_atual