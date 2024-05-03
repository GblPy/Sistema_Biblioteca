
#Importação das Bibliotecas 
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ct
import sqlite3
import re
from datetime import datetime, date

# Definir tema personalizado
ct.set_default_color_theme('./custom_theme.json') 
ct.set_appearance_mode('Dark')

# Função para validar E-mail
def validar_email(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(regex, email))

#Função Verifica tamanho da senha    
def verificar_tamanho_senha(senha):
    return len(senha) > 6

#Função Verifica se os campos não estão vazios
def verificar_campos_vazios(campo):
    return len(campo.strip()) != 0 and not campo.isdigit()

#Função Verifica se o campo é numérico
def verifica_campos_numericos(campo):
    return campo.isnumeric()

# Função para verificar telefone    
def validar_telefone(telefone):
    padrao_telefone = r"\(\d{2}\)\s\d{4,5}-\d{4}"
    return bool(re.match(padrao_telefone, telefone))

#Função para validar data
def validar_data(data_str):
    # Expressão regular para validar o formato da data (dd/mm/aaaa)
    padrao_data = r'\d{2}/\d{2}/\d{4}'

    # Verifica se a string corresponde ao padrão regex
    if not re.match(padrao_data, data_str):
        return False
    # Tenta converter a string para um objeto datetime
    try:
        datetime.strptime(data_str, '%d/%m/%Y')
        return True
    except ValueError:
        return False

#Classe cadastro usuario
class CadastroUsuarioApp:
    #Função inicializadora
    def __init__(self, login_app, cadastro):
        self.login_app = login_app
        self.cadastro = cadastro
        self.cadastro.geometry('1200x600')
        self.cadastro.title("Cadastro de Usuário")
        # Criar widgets
        self.label_biblioteca_cd = ct.CTkLabel(self.cadastro, text="Biblioteca da Cidade", font=ct.CTkFont('Century', 45, weight='bold'), width=50, height=25)
        self.label_biblioteca_cd.pack(padx=10, pady=10)

        self.label_password = ct.CTkLabel(self.cadastro, text="Se Cadastre Aqui!", anchor='center', font=('Arial', 17))
        self.label_password.pack(padx=20, pady=10)

        self.entry_name = ct.CTkEntry(self.cadastro, placeholder_text="Nome Completo", width=400)
        self.entry_name.pack(padx=10, pady=10)

        self.entry_senha = ct.CTkEntry(self.cadastro, placeholder_text="Senha do Usuário (Deve conter mais que 6 caracteres)", show="*", width=400)
        self.entry_senha.pack(padx=10, pady=10)
        
        self.entry_email = ct.CTkEntry(self.cadastro, placeholder_text="Digite seu melhor E-mail", width=400)
        self.entry_email.pack(padx=10, pady=10)
        
        self.entry_tel = ct.CTkEntry(self.cadastro, placeholder_text="Digite seu telefone para contato no formato (xx) xxxxx-xxxx", width=400)
        self.entry_tel.pack(padx=10, pady=10)

        self.button_validar_cad = ct.CTkButton(self.cadastro, text="Validar Cadastro", command=self.cadastrar_usuario, anchor='center', corner_radius=32,
                                               border_color='lightblue', border_width=2, fg_color='transparent')
        self.button_validar_cad.pack(padx=10, pady=(10))
    #Função para cadastro de usuário 
    def cadastrar_usuario(self):
        # Lógica para processar o cadastro de usuário
        nome = self.entry_name.get()
        senha = self.entry_senha.get()
        email = self.entry_email.get()
        telefone = self.entry_tel.get()
        #verifica se a senha é valida
        if not verificar_tamanho_senha(senha):
            messagebox.showwarning("Senha Inválida", "A senha deve ter mais de 6 caracteres.")
            return
        # verifica se o telefone é valido
        if not validar_telefone(telefone):
            messagebox.showwarning("Erro!", "Por favor insira um número de telefone válido.")
            return
        
        # verifica se o e-mail é valido
        if not validar_email(email):
            messagebox.showwarning("Erro", "E-mail inválido. Por favor, insira um e-mail válido.")
            return
        # Se conecta ao banco de dados
        conexao = sqlite3.connect('banco_biblioteca.db')
        
        cur = conexao.cursor()
        
        cur.execute(" INSERT INTO Usuarios VALUES (:nome, :senha, :email, :telefone)",
                    {
                        'nome': nome,
                        'senha': senha,
                        'email': email,
                        'telefone': telefone
                    }
                    )
        conexao.commit()
        conexao.close()
        
        self.entry_name.delete(0, "end")
        self.entry_senha.delete(0, "end")
        self.entry_email.delete(0, "end")
        self.entry_tel.delete(0, "end")
        
        messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso!")
        self.cadastro.destroy()  # Fecha a janela de cadastro após o cadastro ser concluído
        
        # Voltar para a página de login
        self.login_app.voltar_login()

# Classe de cadastro de livro
class CadastroLivroApp:
    def __init__(self, main_page_app, cadastrolivro):
        self.main_page_app = main_page_app
        self.cadastrolivro = cadastrolivro
        
        self.cadastrolivro.geometry('1200x800')
        self.cadastrolivro.title("Cadastro de Livros")

        # Adicione widgets
        self.label_biblioteca_cd = ct.CTkLabel(self.cadastrolivro, text="Biblioteca da Cidade", font=ct.CTkFont('Century', 45, weight='bold'), width=50, height=25)
        self.label_biblioteca_cd.pack(padx=10, pady=10)

        self.label_cadaslv = ct.CTkLabel(self.cadastrolivro, text="Cadastre Aqui o Livro!", anchor='center', font=('Arial', 17))
        self.label_cadaslv.pack(padx=20, pady=10)

        self.entry_titulolv = ct.CTkEntry(self.cadastrolivro, placeholder_text="Título do Livro", width=400)
        self.entry_titulolv.pack(padx=10, pady=10)

        self.entry_autorlv = ct.CTkEntry(self.cadastrolivro, placeholder_text="Digite o Nome do Autor", width=400)
        self.entry_autorlv.pack(padx=10, pady=10)
        
        self.entry_publicacaolv = ct.CTkEntry(self.cadastrolivro, placeholder_text="Ano de Publicação", width=400)
        self.entry_publicacaolv.pack(padx=10, pady=10)
        
        self.entry_ncopiaslv = ct.CTkEntry(self.cadastrolivro, placeholder_text="Número de Cópias", width=400)
        self.entry_ncopiaslv.pack(padx=10, pady=10)

        self.button_validar_cadlv = ct.CTkButton(self.cadastrolivro, text="Validar Cadastro do Livro", command=self.cadastrar_livrobd, anchor='center',
                                                 corner_radius=32, border_color='lightblue', border_width=2, fg_color='transparent')
        self.button_validar_cadlv.pack(padx=10, pady=(10))

        self.button_voltar_main = ct.CTkButton(self.cadastrolivro, text="Voltar a Página Principal", command=self.voltar_pagina_principal, anchor='center', corner_radius=32,
                                        border_color='lightblue', border_width=2, fg_color='transparent')
        self.button_voltar_main.pack(padx=10, pady=(10))
    # Função para voltar a página inicial   
    def voltar_pagina_principal(self):    
        # Fechar a janela atual de empréstimo de livro, se existir
        if hasattr(self, 'cadastrolivro'):
            self.cadastrolivro.destroy()
        
        # Mostrar a página principal novamente
        if hasattr(self, 'main_page_app'):
            self.main_page_app.show_main_page()    
    # Função para cadastrar livro no banco de dados       
    def cadastrar_livrobd(self):
        nomelv = self.entry_titulolv.get()
        autorlv = self.entry_autorlv.get()
        anolv = self.entry_publicacaolv.get()
        n_copiaslv = self.entry_ncopiaslv.get()
        
        if not verificar_campos_vazios(nomelv):
            messagebox.showwarning("Campo Vazio", "Campo precisa conter o Título do Livro.")
            return
        
        if not verificar_campos_vazios(autorlv):
            messagebox.showwarning("Campo Vazio", "Campo precisa conter o Autor do Livro.")
            return
        
        if not verifica_campos_numericos(anolv):
            messagebox.showwarning("Erro", "Digite o Ano do Livro com Números.")
            return
        
        if not verifica_campos_numericos(n_copiaslv):
            messagebox.showwarning("Erro", "Digite o Número de cópias do livro.")
            return
        
        conexao = sqlite3.connect('banco_biblioteca.db')
        cur = conexao.cursor()
        cur.execute("INSERT INTO CadastrosDeLivros (titulo, autor, ano_publicacao, numero_copias) VALUES (?, ?, ?, ?)", (nomelv, autorlv, anolv, n_copiaslv))
        conexao.commit()
        conexao.close()
        
        self.entry_titulolv.delete(0, "end")
        self.entry_autorlv.delete(0, "end")
        self.entry_publicacaolv.delete(0, "end")
        self.entry_ncopiaslv.delete(0, "end")
        
        messagebox.showinfo("Cadastro", "Livro cadastrado com sucesso!")
        self.cadastrolivro.destroy()  # Fecha a janela de cadastro após o cadastro ser concluído
        
        # Volta para a página principal
        self.main_page_app.show_main_page()
        
# Classe de emprestimo do livro
class EmprestimoLivroApp:
    def __init__(self, main_page_app, emprestimolivro, user_info):
        self.main_page_app = main_page_app
        self.emprestimolv = emprestimolivro
        self.user_info = user_info  # Recebe as informações do usuário

        self.emprestimolv.geometry('1200x800')
        self.emprestimolv.title("Empréstimo de Livros")

        # Adicione widgets 
        self.label_biblioteca_cd = ct.CTkLabel(self.emprestimolv, text="Biblioteca da Cidade", font=ct.CTkFont('Century', 45, weight='bold'), width=50, height=25)
        self.label_biblioteca_cd.pack(padx=10, pady=10)

        self.label_locacaolv = ct.CTkLabel(self.emprestimolv, text="Locação de Livro !", anchor='center', font=('Arial', 17))
        self.label_locacaolv.pack(padx=20, pady=10)

        self.entry_procuralv = ct.CTkEntry(self.emprestimolv, placeholder_text="Qual nome do Livro que deseja?", width=400)
        self.entry_procuralv.pack(padx=10, pady=10)
        
        self.entry_data_devlv = ct.CTkEntry(self.emprestimolv, placeholder_text="Qual será a data de devolução?(Dia/Mês/Ano)", width=400)
        self.entry_data_devlv.pack(padx=10, pady=10)

        self.button_validar_emprestimolv = ct.CTkButton(self.emprestimolv, text="Buscar Livro e verificar se está disponível", command=self.emprestimo_livrobd, anchor='center', corner_radius=32,
                                        border_color='lightblue', border_width=2, fg_color='transparent')
        self.button_validar_emprestimolv.pack(padx=10, pady=(10))

        self.button_voltar_main = ct.CTkButton(self.emprestimolv, text="Voltar a Página Principal", command=self.voltar_pagina_principal, anchor='center', corner_radius=32,
                                        border_color='lightblue', border_width=2, fg_color='transparent')
        self.button_voltar_main.pack(padx=10, pady=(10))
    
    def voltar_pagina_principal(self):    
        # Fechar a janela atual de empréstimo de livro, se existir
        if hasattr(self, 'emprestimolv'):
            self.emprestimolv.destroy()
        
        # Mostrar a página principal novamente
        if hasattr(self, 'main_page_app'):
            self.main_page_app.show_main_page()
      
    def emprestimo_livrobd(self):
        # Obter os dados inseridos pelo usuário
        titulo_livro = self.entry_procuralv.get()
        data_devolucao_str = self.entry_data_devlv.get()
        
        # Verificar se os campos estão preenchidos
        if not verificar_campos_vazios(titulo_livro):
            messagebox.showwarning("Campo Vazio", "Por favor, insira o título do livro.")
            return
        
        if not verificar_campos_vazios(data_devolucao_str):
            messagebox.showwarning("Campo Vazio", "Por favor, insira a data de devolução.")
            return

        # Verificar a validade da data de devolução
        try:
            data_devolucao = datetime.strptime(data_devolucao_str, '%d/%m/%Y').date()
            data_atual = datetime.now().date()
            
            if data_devolucao < data_atual:
                messagebox.showerror("Erro", "A data de devolução deve ser igual ou posterior à data atual.")
                return
        except ValueError:
            messagebox.showerror("Erro", "Formato de data inválido. Use o formato DD/MM/AAAA.")
            return

        # Conectar ao banco de dados
        conexao = sqlite3.connect('banco_biblioteca.db')
        cur = conexao.cursor()
        
        try:
            # Verificar se há cópias disponíveis do livro
            cur.execute("SELECT numero_copias FROM CadastrosDeLivros WHERE titulo = ?", (titulo_livro,))
            resultado_copias = cur.fetchone()
            
            if resultado_copias:
                numero_copias = resultado_copias[0]
                if numero_copias > 0:
                    # Verificar se o usuário já tem um livro com o mesmo título emprestado
                    cur.execute("SELECT * FROM Emprestimos WHERE nome_completo = ? AND livro_locado = ?", (self.user_info['nome_completo'], titulo_livro))
                    resultado_emprestimo = cur.fetchone()
                    
                    if resultado_emprestimo:
                        messagebox.showinfo("Livro Já Emprestado", f"Você já tem o livro '{titulo_livro}' emprestado.")
                        return
                    
                    # Registrar a data de locação como a data atual
                    data_locacao = datetime.today().strftime('%d/%m/%Y')
                    
                    # Obter o nome do usuário logado
                    nome_usuario = self.user_info['nome_completo']

                    # Iniciar uma transação para garantir a consistência dos dados
                    cur.execute("BEGIN TRANSACTION")
                    
                    # Atualizar o número de cópias e a data de locação para o livro em questão
                    cur.execute("UPDATE CadastrosDeLivros SET numero_copias = numero_copias - 1 WHERE titulo = ?", (titulo_livro,))
                    
                    # Registrar o empréstimo na tabela Emprestimos
                    cur.execute("INSERT INTO Emprestimos (nome_completo, livro_locado, data_locacao, data_devolucao) VALUES (?, ?, ?, ?)", (nome_usuario, titulo_livro, data_locacao, data_devolucao))
                    # Confirmar a transação
                    cur.execute("COMMIT")
                    
                    # Exibir mensagem de sucesso e retornar à página principal
                    messagebox.showinfo("Sucesso", f"Empréstimo do livro '{titulo_livro}' realizado com sucesso!")
                    self.emprestimolv.destroy()  # Fechar a janela de empréstimo
                    self.main_page_app.show_main_page()  # Voltar para a página principal
                else:
                    messagebox.showinfo("Sem Cópias Disponíveis", "Desculpe, não há cópias disponíveis deste livro.")
            else:
                messagebox.showinfo("Livro Não Encontrado", f"O livro '{titulo_livro}' não foi encontrado no banco de dados.")
        except Exception as e:
            # Em caso de erro, reverter a transação e exibir uma mensagem de erro
            conexao.rollback()
            messagebox.showerror("Erro", f"Ocorreu um erro ao realizar o empréstimo: {str(e)}")
        finally:
            # Fechar a conexão com o banco de dados
            conexao.close()

# Classe da aplicação de devolução do livro
class DevolucaoLivroApp:
    def __init__(self, main_page_app, devolucaolivro, user_info):
        self.main_page_app = main_page_app
        self.devolucaolv = devolucaolivro
        self.user_info = user_info  # Recebe as informações do usuário
        
        self.devolucaolv.geometry('1200x800')
        self.devolucaolv.title("Empréstimo de Livros")

        # Adicione widgets para o cadastro de usuário aqui
        self.label_biblioteca_cd = ct.CTkLabel(self.devolucaolv, text="Biblioteca da Cidade", font=ct.CTkFont('Century', 45, weight='bold'), width=50, height=25)
        self.label_biblioteca_cd.pack(padx=10, pady=10)

        self.label_devlv = ct.CTkLabel(self.devolucaolv, text="Devolução de Livro !", anchor='center', font=('Arial', 17))
        self.label_devlv.pack(padx=20, pady=10)

        self.entry_devolvelv = ct.CTkEntry(self.devolucaolv, placeholder_text="Qual nome do Livro que deseja efetuar a devolução?", width=400)
        self.entry_devolvelv.pack(padx=10, pady=10)
       
        self.button_validar_devolucaolv = ct.CTkButton(self.devolucaolv, text="Efetuar Devolução do Livro", command=self.devolucao_livrobd, anchor='center', corner_radius=32,
                                        border_color='lightblue', border_width=2, fg_color='transparent')
        self.button_validar_devolucaolv.pack(padx=10, pady=(10))

        self.button_voltar_main = ct.CTkButton(self.devolucaolv, text="Voltar a Página Principal", command=self.voltar_pagina_principal, anchor='center', corner_radius=32,
                                        border_color='lightblue', border_width=2, fg_color='transparent')
        self.button_voltar_main.pack(padx=10, pady=(10))
    
    def voltar_pagina_principal(self):    
        # Fechar a janela atual de devolução de livro, se existir
        if hasattr(self, 'devolucaolv'):
            self.devolucaolv.destroy()
        
        # Mostrar a página principal novamente
        if hasattr(self, 'main_page_app'):
            self.main_page_app.show_main_page()
      
    def devolucao_livrobd(self):
        titulo_livro = self.entry_devolvelv.get()
        
        if not verificar_campos_vazios(titulo_livro):
            messagebox.showwarning("Campo Vazio", "Campo precisa conter o Título do Livro.")
            return
        
        conexao = sqlite3.connect('banco_biblioteca.db')
        cur = conexao.cursor()
        
        try:
            # Verificar se o usuário tem o livro alugado
            cur.execute("SELECT * FROM Emprestimos WHERE nome_completo = ? AND livro_locado = ? AND confirma_devolucao IS NULL", (self.user_info['nome_completo'], titulo_livro))
            resultado = cur.fetchone()
            
            if resultado:
                # Atualizar o número de cópias disponíveis para o livro
                cur.execute("UPDATE CadastrosDeLivros SET numero_copias = numero_copias + 1 WHERE titulo = ?", (titulo_livro,))
                
                # Marcar a devolução do livro na tabela Emprestimos
                cur.execute("UPDATE Emprestimos SET confirma_devolucao = 1 WHERE nome_completo = ? AND livro_locado = ?", (self.user_info['nome_completo'], titulo_livro))
                
                conexao.commit()
                conexao.close()
                messagebox.showinfo("Devolução Realizada", f"Livro '{titulo_livro}' devolvido com sucesso!")
            else:
                messagebox.showwarning("Livro Não Alugado", f"Você não possui o livro '{titulo_livro}' alugado.")
        except Exception as e:
            conexao.rollback()
            messagebox.showerror("Erro", f"Ocorreu um erro ao realizar a devolução: {str(e)}")
        finally:
            conexao.close()

        self.entry_devolvelv.delete(0, "end")   # Limpar o campo de entrada


# Classe da aplicação de consulta do livro
class ConsultaLivroApp:
    def __init__(self, main_page_app, consultalivro):
        self.main_page_app = main_page_app
        self.consultalv = consultalivro
        self.consultalv.geometry('1200x800')
        self.consultalv.title("Empréstimo de Livros")

        # Adicione widgets para o cadastro de usuário aqui
        self.label_biblioteca_cd = ct.CTkLabel(self.consultalv, text="Biblioteca da Cidade", font=ct.CTkFont('Century', 45, weight='bold'), width=50, height=25)
        self.label_biblioteca_cd.pack(padx=10, pady=10)

        self.label_consultalv = ct.CTkLabel(self.consultalv, text="Consulta de Livro !", anchor='center', font=('Arial', 17))
        self.label_consultalv.pack(padx=20, pady=10)

        #Tela de consulta
        self.resultado_tree = ttk.Treeview(self.consultalv, columns=("Nome do Livro", "Autor", "Ano de Publicação"))
        self.resultado_tree.pack(side="top", padx=5, pady=5, expand=True, fill="both")
        self.resultado_tree.heading("#0", text="ID")
        self.resultado_tree.heading("Nome do Livro", text="Nome do Livro")
        self.resultado_tree.heading("Autor", text="Autor")
        self.resultado_tree.heading("Ano de Publicação", text="Ano de Publicação")
        
        self.entry_consultalv = ct.CTkEntry(self.consultalv, placeholder_text="Consulte o Livro que deseja?", width=400)
        self.entry_consultalv.pack(padx=10, pady=10)
        
        self.button_validar_consultalv = ct.CTkButton(self.consultalv, text="Consultar !", command=self.pesquisar_livrosbd, anchor='center', corner_radius=32,
                                        border_color='lightblue', border_width=2, fg_color='transparent')
        self.button_validar_consultalv.pack(padx=10, pady=(10))

        self.button_voltar_main = ct.CTkButton(self.consultalv, text="Voltar a Página Principal", command=self.voltar_pagina_principal, anchor='center', corner_radius=32,
                                        border_color='lightblue', border_width=2, fg_color='transparent')
        self.button_voltar_main.pack(padx=10, pady=(10))
    
    def voltar_pagina_principal(self):    
        # Fechar a janela atual de empréstimo de livro, se existir
        if hasattr(self, 'consultalv'):
            self.consultalv.destroy()
        
        # Mostrar a página principal novamente
        if hasattr(self, 'main_page_app'):
            self.main_page_app.show_main_page()
    
      
    def pesquisar_livrosbd(self):
        # Limpar os resultados anteriores
        for row in self.resultado_tree.get_children():
            self.resultado_tree.delete(row)
        
        # Recuperar o critério de pesquisa
        termo_pesquisa = self.entry_consultalv.get()
        
        # Construir a consulta SQL baseada no critério de 
        conexao = sqlite3.connect('banco_biblioteca.db')
        cur = conexao.cursor()
        
        # Construir a consulta SQL baseada no critério de pesquisa
        consulta_sql = "SELECT * FROM CadastrosDeLivros WHERE titulo LIKE ? OR autor LIKE ? OR ano_publicacao = ?"
        parametros = (f"%{termo_pesquisa}%", f"%{termo_pesquisa}%", termo_pesquisa)

        # Executar a consulta SQL
        cur.execute(consulta_sql, parametros)
        resultados = cur.fetchall()

        # Exibir os resultados na Treeview
        for i, row in enumerate(resultados):
            self.resultado_tree.insert("", "end", text=i+1, values=row)
            
            
#Classe da aplicação de Relatorio da Biblioteca
class RelatorioApp:
    def __init__(self, main_page_app, relatorio):
        self.main_page_app = main_page_app
        self.relatorio = relatorio
        self.relatorio.geometry('1200x800')
        self.relatorio.title("Empréstimo de Livros")

        # Adicione widgets para o relatório da biblioteca aqui
        self.label_biblioteca_cd = ct.CTkLabel(self.relatorio, text="Biblioteca da Cidade", font=ct.CTkFont('Century', 45, weight='bold'), width=50, height=25)
        self.label_biblioteca_cd.pack(padx=2, pady=2)

        self.label_relatorio_biblioteca = ct.CTkLabel(self.relatorio, text="Relatório da Biblioteca !", anchor='center', font=('Arial', 17))
        self.label_relatorio_biblioteca.pack(padx=5, pady=5)
        
        # Treeview para livros disponíveis
        self.label_livros_dispo = ct.CTkLabel(self.relatorio, text="Livros Disponíveis", anchor='center', font=('Arial', 15))
        self.label_livros_dispo.pack(padx=5, pady=5)
        self.treeview_livros_disponiveis = ttk.Treeview(self.relatorio, columns=("Título", "Autor", "Ano de Publicação"), height=5)
        self.treeview_livros_disponiveis.pack(padx=40, pady=5, expand=True, fill="both")
        self.treeview_livros_disponiveis.column("#0", width=0)
        self.treeview_livros_disponiveis.heading("Título", text="Título")
        self.treeview_livros_disponiveis.heading("Autor", text="Autor")
        self.treeview_livros_disponiveis.heading("Ano de Publicação", text="Ano de Publicação")
        
        # Treeview para livros emprestados
        self.label_livros_empre = ct.CTkLabel(self.relatorio, text="Livros Emprestados", anchor='center', font=('Arial', 15))
        self.label_livros_empre.pack(padx=5, pady=5)
        self.treeview_livros_emprestados = ttk.Treeview(self.relatorio, columns=("Alugado Por", "Título do Livro", "Data da Locação"), height=5)
        self.treeview_livros_emprestados.pack(padx=40, pady=5, expand=True, fill="both")
        self.treeview_livros_emprestados.column("#0", width=0)
        self.treeview_livros_emprestados.heading("Alugado Por", text="Alugado Por")
        self.treeview_livros_emprestados.heading("Título do Livro", text="Título do Livro")
        self.treeview_livros_emprestados.heading("Data da Locação", text="Data da Locação")
        
        # Treeview para Usuários
        self.label_usuarios = ct.CTkLabel(self.relatorio, text="Usuários", anchor='center', font=('Arial', 15))
        self.label_usuarios.pack(padx=5, pady=5)
        self.treeview_usuarios = ttk.Treeview(self.relatorio, columns=("Nome", "E-mail", "Telefone"), height=5)
        self.treeview_usuarios.pack(padx=40, pady=5, expand=True, fill="both")
        self.treeview_usuarios.column("#0", width=0)
        self.treeview_usuarios.heading("Nome", text="Nome")
        self.treeview_usuarios.heading("E-mail", text="E-mail")
        self.treeview_usuarios.heading("Telefone", text="Telefone")
        
        
        self.button_voltar_main = ct.CTkButton(self.relatorio, text="Voltar a Página Principal", command=self.voltar_pagina_principal, anchor='center', corner_radius=32, border_color='lightblue', border_width=2, fg_color='transparent')
        self.button_voltar_main.pack(padx=90, pady=10)
        
        # Chama o método para carregar os livros disponíveis
        self.relatoriobd()
    
    def voltar_pagina_principal(self):    
        # Fechar a janela atual de empréstimo de livro, se existir
        if hasattr(self, 'relatorio'):
            self.relatorio.destroy()
        
        # Mostrar a página principal novamente
        if hasattr(self, 'main_page_app'):
            self.main_page_app.show_main_page()
    
    def relatoriobd(self):        
        conexao = sqlite3.connect('banco_biblioteca.db')
        cur = conexao.cursor()
        
        # Consulta SQL para livros disponíveis
        consulta_livros_disponiveis = "SELECT * FROM CadastrosDeLivros WHERE numero_copias >= 1"
        cur.execute(consulta_livros_disponiveis)
        livros_disponiveis = cur.fetchall()
        
        # Exibir os resultados na Treeview de livros disponíveis
        for row in livros_disponiveis:
            self.treeview_livros_disponiveis.insert("", "end", values=row)
        
        # Consulta SQL para livros emprestados que ainda não foram devolvidos
        consulta_livros_emprestados = "SELECT * FROM Emprestimos WHERE confirma_devolucao IS NULL"
        cur.execute(consulta_livros_emprestados)
        livros_emprestados = cur.fetchall()
        
        # Exibir os resultados na Treeview de livros emprestados
        for row in livros_emprestados:
            self.treeview_livros_emprestados.insert("", "end", values=row)
            
        # Consulta SQL para Usuários
        consulta_usuarios = "SELECT nome_completo, email, telefone FROM Usuarios"
        cur.execute(consulta_usuarios)
        usuarios = cur.fetchall()
        
        # Exibir os resultados na Treeview de usuários
        for row in usuarios:
           self.treeview_usuarios.insert("", "end", values=row)

        

        # Fechar a conexão com o banco de dados
        conexao.close()


# Classe da aplicação da página principal
class MainPageApp:
    def __init__(self, login_app, user_info):
        self.login_app = login_app
        self.user_info = user_info # Armazena as informações do usuário logado
    
    def show_main_page(self):
    # Criar e exibir a janela da página principal
        self.main_window = ct.CTk()
        self.main_window.geometry('1200x800')
        self.main_window.title("Página Inicial")

        # Adicione widgets e funcionalidades à sua página principal aqui
        #CONFIGURA O LAYOUT(4X4)
        self.main_window.grid_columnconfigure(1, weight=1)
        self.main_window.grid_columnconfigure((2, 3), weight=0)
        self.main_window.grid_rowconfigure((0, 1, 3), weight=1)
        
        #CRIANDO SIDEBAR FRAME PARA AREAS DO APP
        self.sidebar_frame = ct.CTkFrame(self.main_window, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky='nsew')
        self.sidebar_frame.grid_rowconfigure(6, weight=1)
        
        self.logo_label = ct.CTkLabel(self.sidebar_frame, text="Biblioteca da Cidade", font=ct.CTkFont('Century', 20, weight='bold'))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        self.sidebar_button1 = ct.CTkButton(self.sidebar_frame, text="Cadastro de Livros", font=ct.CTkFont(size=17), corner_radius=32, command=self.cadastrar_livro)
        self.sidebar_button1.grid(row=1, column=0, padx=20, pady=10)
        
        self.sidebar_button2 = ct.CTkButton(self.sidebar_frame, text="Empréstimo de Livros", font=ct.CTkFont(size=17), corner_radius=32, command=self.emprestimo_livro)
        self.sidebar_button2.grid(row=2, column=0, padx=20, pady=10)
        
        self.sidebar_button3 = ct.CTkButton(self.sidebar_frame, text="Devolução de Livros", font=ct.CTkFont(size=17), corner_radius=32, command=self.devolucao_livro)
        self.sidebar_button3.grid(row=3, column=0, padx=20, pady=10)
        
        self.sidebar_button4 = ct.CTkButton(self.sidebar_frame, text="Consulta de Livros", font=ct.CTkFont(size=17), corner_radius=32, command=self.consulta_livro)
        self.sidebar_button4.grid(row=4, column=0, padx=10, pady=10)
        
        self.sidebar_button5 = ct.CTkButton(self.sidebar_frame, text="Relatório Biblioteca", font=ct.CTkFont(size=17), corner_radius=32, command=self.relatorio_biblioteca)
        self.sidebar_button5.grid(row=5, column=0, padx=20, pady=10)
        
        self.sidebar_button6 = ct.CTkButton(self.sidebar_frame, text="Voltar Login", font=ct.CTkFont(size=17), corner_radius=32, command=self.voltar_login)
        self.sidebar_button6.grid(row=6, column=0, padx=20, pady=10)
        
        self.appearance_mode_label = ct.CTkLabel(self.sidebar_frame, text='Modo de Aparência:', anchor='w')
        self.appearance_mode_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionmenu = ct.CTkOptionMenu(self.sidebar_frame, values=['Dark', 'Light'],
                                                           command=self.change_appearance_mode_event)
        self.appearance_mode_optionmenu.grid(row=8, column=0, padx=20, pady=(10, 10))
        
        self.scaling_label = ct.CTkLabel(self.sidebar_frame, text='UI Escala:', anchor='w')
        self.scaling_label.grid(row=9, column=0, padx=20, pady=(10, 0))
        self.scaling_optionmenu = ct.CTkOptionMenu(self.sidebar_frame, values=['80%', '90%', '100%', '110%', '120%'],
                                                   command=self.change_scaling_event)
        self.scaling_optionmenu.grid(row=10, column=0, padx=20, pady=(10, 20))
    
        # Adicione widgets e funcionalidades à sua página principal aqui
        self.main_window.mainloop()

    def cadastrar_livro(self):
        cadastrolivro_window = ct.CTkToplevel(self.main_window)
        CadastroLivroApp(self, cadastrolivro_window)
        self.main_window.withdraw()  # Oculta a janela principal
        
    def devolucao_livro(self):
        devolucao_window = ct.CTkToplevel(self.main_window)
        DevolucaoLivroApp(self, devolucao_window, self.user_info)  
        self.main_window.withdraw()  # Oculta a janela principal 
        
    def consulta_livro(self):
        consulta_window = ct.CTkToplevel(self.main_window)
        ConsultaLivroApp(self, consulta_window)  
        self.main_window.withdraw()  # Oculta a janela principal      
        
    def relatorio_biblioteca(self):
        relatorio_window = ct.CTkToplevel(self.main_window)
        RelatorioApp(self, relatorio_window)  
        self.main_window.withdraw()  # Oculta a janela principal          
        
    def emprestimo_livro(self):
        emprestimolv_window = ct.CTkToplevel(self.main_window)
        EmprestimoLivroApp(self, emprestimolv_window, self.user_info)  
        self.main_window.withdraw()  # Oculta a janela principal    
    
    def change_appearance_mode_event(self, new_apperance_mode: str):
        ct.set_appearance_mode(new_apperance_mode)       
        
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace('%', '')) / 100
        ct.set_widget_scaling(new_scaling_float)    
    
    def voltar_login(self):    
        # Fechar a janela principal atual, se existir
        if hasattr(self, 'main_window'):
            self.main_window.destroy()
        # Criar uma nova instância de LoginApp
        new_login_app = LoginApp()
        new_login_app.root.mainloop()  # Iniciar o loop principal da nova instância

# Classe da aplicação de login
class LoginApp:
    def __init__(self):
        self.root = ct.CTk()
        self.root.geometry('1200x600')
        self.root.title("Login")
        self.root.resizable(width=False, height=False)
        self.conexao = sqlite3.connect('banco_biblioteca.db')
        self.cur = self.conexao.cursor()

        # Criar widgets
        self.label_biblioteca_cd = ct.CTkLabel(self.root, text="Biblioteca da Cidade", font=ct.CTkFont('Century', 45, weight='bold'), width=50, height=25)
        self.label_biblioteca_cd.pack(padx=10, pady=10)

        self.label_password = ct.CTkLabel(self.root, text="Seja Bem Vindo !", anchor='center', font=('Arial', 17))
        self.label_password.pack(padx=20, pady=10)

        self.entry_useremail = ct.CTkEntry(self.root, placeholder_text="Login (E-Mail):", width=400)
        self.entry_useremail.pack(padx=10, pady=10)

        self.entry_password = ct.CTkEntry(self.root, placeholder_text="Senha do Usuário:", show="*", width=400)
        self.entry_password.pack(padx=10, pady=10)

        self.button_entrar = ct.CTkButton(self.root, text="Se Conectar", command=self.login, anchor='center', corner_radius=32,
                                        border_color='lightblue', border_width=2, fg_color='transparent')
        self.button_entrar.pack(padx=10, pady=(10))

        self.label_cadastrar = ct.CTkLabel(self.root, text="Não tem uma conta ?\n Crie uma em poucos instantes!", anchor='center', font=ct.CTkFont('Arial', 14, weight='bold'))
        self.label_cadastrar.pack(padx=20, pady=10)

        self.button_cadastrar = ct.CTkButton(self.root, text="Criar Conta", command=self.abrir_pagina_cadastro, anchor='center', corner_radius=32,
                                        border_color='lightblue', border_width=2, fg_color='transparent')
        self.button_cadastrar.pack(padx=10, pady=10)
        
    def abrir_pagina_cadastro(self):
        cadastro_window = ct.CTkToplevel(self.root)
        CadastroUsuarioApp(self, cadastro_window)    
        self.root.withdraw()  # Oculta a janela de login

    def voltar_login(self):
        # Tentar reexibir a janela de login
        try:
            self.root.deiconify()
        except tk.TclError:
            # Fechar a janela principal atual, se existir
            if hasattr(self, 'main_window'):
                self.main_window.destroy()
            # Criar uma nova instância de LoginApp
            new_login_app = LoginApp()
            new_login_app.root.mainloop()  # Iniciar o loop principal da nova instância
    
    def login(self):
        useremail = self.entry_useremail.get()
        password = self.entry_password.get()
        
        self.cur.execute("SELECT * FROM Usuarios WHERE email = ? AND senha = ?", (useremail, password))
        resultado = self.cur.fetchone()
        
        if resultado:
            messagebox.showinfo("Login",  "Login feito com sucesso!")
            # Recupera as informações do usuário
            user_info = {
                'nome_completo': resultado[0],  # Supondo que o nome do usuário está na primeira coluna
                # Adicione outras informações do usuário conforme necessário
            }
            # Abre a tela principal do aplicativo
            main_page_app = MainPageApp(self, user_info)
            self.root.withdraw()  # Oculta a janela de login
            main_page_app.show_main_page()
            
        else:
            messagebox.showerror("Login", "Credenciais inválidas. Tente novamente.")    

# Inicializa o aplicativo
if __name__ == '__main__':
    app = LoginApp()
    app.root.mainloop()
