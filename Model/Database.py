import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("personadb.db")
        self.cursor = self.connection.cursor()

    def create_table(self, table_name, columns):
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")
        self.commit()

    def insert_data(self, table_name, data):
        self.cursor.executemany(f"INSERT INTO {table_name} VALUES ({data})")
        self.commit()

    def get_all_data(self, table_name):
        self.cursor.execute(f"SELECT * FROM {table_name}")
        return self.cursor.fetchall()

    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()


'''cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL
    )
""")
'''
'''usuarios = [
    ("João", "joao@email.com"),
    ("Maria", "maria@email.com"),
    ("Pedro", "pedro@email.com")
]'''

'''cursor.executemany("""
    INSERT INTO usuarios (nome, email)
    VALUES (?, ?)
""", usuarios)
'''
'''
cursor.execute("""
    SELECT id, nome, email
    FROM usuarios
""")
'''