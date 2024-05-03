import pandas as pd
import sqlite3


conexao = sqlite3.connect("banco_biblioteca.db")

cur = conexao.cursor()

cur.execute("""CREATE TABLE Emprestimos(
    nome_completo text,
    livro_locado text,
    data_locacao text,
    data_devolucao text,
    confirma_devolucao text
    )
 """)

conexao.commit()
conexao.close()