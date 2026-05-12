import sqlite3

conexao = sqlite3.connect("data/alunos.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    n1 REAL,
    n2 REAL,
    media REAL,
    situacao TEXT
)
""")

conexao.commit()

def cadastrar_aluno(nome, n1, n2, media, situacao):
    cursor.execute(
        "INSERT INTO alunos (nome, n1, n2, media, situacao) VALUES (?, ?, ?, ?, ?)",
        (nome, n1, n2, media, situacao)
    )
    conexao.commit()