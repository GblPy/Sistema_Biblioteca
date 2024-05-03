# Sistema_Biblioteca
 

Sistema de Empréstimo de Livros
O Sistema de Empréstimo de Livros é uma aplicação desenvolvida em Python, projetada para facilitar a gestão de empréstimos e devoluções de livros em bibliotecas municipais. Esta aplicação oferece uma interface intuitiva e eficiente para usuários realizarem empréstimos, devoluções e consultas de disponibilidade de livros.

Funcionalidades
1. Cadastro de Usuários
Permite o registro de novos usuários na biblioteca, coletando informações como nome completo, E-mail, senha e telefone (todos os campos contém um tipo de verificação).

2. Cadastro de Livros
Permite o registro de novos livros na biblioteca, incluindo detalhes como título, autor e número de cópias disponíveis.

3. Empréstimo de Livros
Usuários podem realizar empréstimos de livros disponíveis na biblioteca, efetuando a pesquisa de livros disponíveis e definindo uma data de devolução (isso se o livro tiver disponível e se os campos for digitado corretamente, já é registrado automaticamente data de empréstimo no banco de dados caso houver disponibilidade).

4. Devolução de Livros
Facilita a devolução dos livros emprestados, registrando a data de devolução no banco de dados e atualizando a disponibilidade do livro na biblioteca (contém verificação no campo de devolução, que vê se o usuário tem tal livro alugado).

5. Verificação de Disponibilidade
Usuários podem verificar a disponibilidade de um livro específico na biblioteca antes de realizar o empréstimo (apenas clicando no botão de relatorio da biblioteca).

Requisitos
Python 3.x

Bibliotecas:
Tkinter (geralmente incluída na instalação padrão do Python)
CustomTkinter
Datetime
sqlite3

Como Usar
Clonar o Repositório: Clone ou faça o download deste repositório para o seu sistema.
Instalar Dependências: Certifique-se de ter Python instalado em seu sistema. Se necessário, instale as bibliotecas que está acima.
Executar o Aplicativo: Abra um terminal na pasta do projeto e execute o seguinte comando:
bash
Copy code
python Gui.py
Utilizar a Interface Gráfica: O aplicativo será aberto, permitindo que você navegue pelas diferentes funcionalidades usando a interface gráfica.
Desenvolvimento
O Sistema de Empréstimo de Livros foi desenvolvido em Python, utilizando o framework Tkinter para a criação da interface gráfica. A estrutura do código é organizada em classes para facilitar a manutenção e escalabilidade do sistema.

As principais etapas do código incluem:

Inicialização da Interface Gráfica: Configuração da interface principal do aplicativo, incluindo widgets para entrada de dados e botões de ação.
Funcionalidades do Sistema: Implementação das funcionalidades principais do sistema, como login, cadastro de usuários, cadastro de livros, consulta de livros, relatorio da biblioteca, empréstimo e devolução de livros.
Conexão com o Banco de Dados: Utilização do banco de dados SQLite para armazenar e gerenciar os dados do sistema, garantindo a persistência e integridade dos dados.
