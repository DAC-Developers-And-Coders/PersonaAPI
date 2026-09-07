import sqlite3
import Utils.default_values as df

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("personadb.db", check_same_thread=False)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON")

    def initialize_database(self):
        self.create_table('Arcana', 'id INTEGER PRIMARY KEY, '
                                    'nome TEXT NOT NULL, '
                                    'descricao TEXT')

        self.create_table('Elemento', 'id INTEGER PRIMARY KEY, nome VARCHAR(50) NOT NULL')

        self.create_table('Persona', 'id INTEGER PRIMARY KEY AUTOINCREMENT, '
                                     'nome TEXT NOT NULL, '
                                     'origem TEXT, '
                                     'primeira_aparicao TEXT, '
                                     'classe TEXT, '
                                     'nivel_inicial INTEGER, '
                                     'arcana_id INTEGER NOT NULL, '
                                     'elemento_id INTEGER NOT NULL, '
                                     'FOREIGN KEY (arcana_id) REFERENCES Arcana(id), '
                                     'FOREIGN KEY (elemento_id) REFERENCES Elemento(id)')

        self.insert_default_values()

    def insert_default_values(self):
        if not self.verify_table_data('Arcana'):
            for arcana in df.arcanas:
                self.insert_data('Arcana', arcana)

        if not self.verify_table_data('Elemento'):
            for elemento in df.elementos:
                self.insert_data('Elemento', elemento)

    def create_table(self, table_name, columns):
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")
        self.commit()

    def insert_data(self, table_name, data):
        columns = ', '.join(data.keys())
        placeholders = ', '.join('?' for _ in data)

        self.cursor.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})", list(data.values()))
        self.commit()

        return self.cursor.lastrowid

    def update_data(self, table_name, data, element_id):
        columns = ', '.join(f'{column} = ?' for column in data.keys())

        values = list(data.values())
        values.append(element_id)

        self.cursor.execute(f"UPDATE {table_name} SET {columns} WHERE id = ?", values)
        self.commit()

    def update_specific_attribute(self, table_name, attribute, value, element_id):
        self.cursor.execute(f"UPDATE {table_name} SET {attribute} = ? WHERE id = ?", (value, element_id))
        self.commit()

    def get_all_data(self, table_name):
        if table_name == 'Persona':
            self.cursor.execute(f"SELECT p.*, a.nome AS nome_arcana, e.nome AS nome_elemento FROM {table_name} p "
                                f"JOIN Arcana a ON p.arcana_id = a.id "
                                f"JOIN Elemento e ON p.elemento_id = e.id")
        else:
            self.cursor.execute(f"SELECT * FROM {table_name}")

        return [dict(row) for row in self.cursor.fetchall()]

    def get_specific_data(self, table_name, column, value):
        if table_name == 'Persona': 
            self.cursor.execute(f"SELECT p.*, a.nome AS nome_arcana, e.nome AS nome_elemento FROM {table_name} p "
                                f"JOIN Arcana a ON p.arcana_id = a.id "
                                f"JOIN Elemento e ON p.elemento_id = e.id "
                                f"WHERE p.{column} = ?", (value,))
        else:
            self.cursor.execute(f"SELECT * FROM {table_name} WHERE {column} = ?", (value,))

        row = self.cursor.fetchone()

        if not row:
            return None

        return dict(row)

    def delete_data(self, table_name, element_id):
        self.cursor.execute(f"DELETE FROM {table_name} WHERE id = ?", (element_id,))
        self.commit()

    def verify_table_data(self, table_name):
        self.cursor.execute(f"SELECT 1 FROM {table_name} LIMIT 1")
        return self.cursor.fetchone()

    def verify_specific_value(self, table_name, element_id):
        self.cursor.execute(f"SELECT 1 FROM {table_name} WHERE id = ?", (element_id,))
        return self.cursor.fetchone()

    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()