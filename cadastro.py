
import sqlite3


conexao = sqlite3.connect("banco_biblioteca.db")

cur = conexao.cursor()

cur.execute("""CREATE TABLE Usuarios(
    nome_completo text,
    senha text,
    email text,
    telefone text
    )
 """)

conexao.commit()
conexao.close()