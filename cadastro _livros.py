import sqlite3

# conecta ao banco de dados 
conexao = sqlite3.connect('banco_biblioteca.db')

# cria um cursor para executar as operações
cur = conexao.cursor()

# executa as instruções no banco
cur.execute("""CREATE TABLE IF NOT EXISTS CadastrosDeLivros(
    titulo TEXT NOT NULL,
    autor  TEXT NOT NULL,
    ano_publicacao INTEGER NOT NULL,
    numero_copias  INTEGER NOT NULL)
            """)

conexao.commit()
conexao.close()