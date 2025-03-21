URL Shortener 🔗
Este é um projeto simples de encurtador de URLs desenvolvido com as seguintes tecnologias:

Frontend: HTML, CSS e JavaScript
Backend: Python (Flask)
Banco de Dados: SQLite
📋 Funcionalidades
Encurtar URLs longas.
Redirecionar URLs encurtadas para o endereço original.
Interface simples e amigável.
🚀 Como rodar o projeto
Siga as instruções abaixo para configurar e executar o projeto localmente.

Pré-requisitos
Você precisará ter instalado:

Python 3.7 ou superior
Um navegador atualizado
Passo a passo
Clone este repositório:

git clone git@github.com:matuza1977/shirinker.git
cd url-shortener
Crie um ambiente virtual:

python -m venv venv
Ative o ambiente virtual:

No Linux/macOS:
source venv/bin/activate
No Windows:
venv\Scripts\activate
Instale as dependências:

pip install flask
Execute o aplicativo:

python app.py
Acesse no navegador: Abra o navegador e entre no endereço: http://127.0.0.1:5000/

📂 Estrutura do Projeto
url-shortener/
├── static/
│   ├── style.css       # Estilização da aplicação
│   ├── script.js       # JavaScript do frontend
├── templates/
│   ├── index.html      # Página principal do sistema
├── app.py              # Backend com Flask
├── database.db         # Banco de dados SQLite
├── README.md           # Documentação do projeto
📚 Tecnologias Utilizadas
Flask: Framework Python para web.
HTML: Estrutura da página.
CSS: Estilização customizada.
JavaScript: Comunicação com o servidor através de requisições assíncronas.
SQLite: Banco de dados local.
✨ Funcionalidades Futuras (Se desejar melhorar o projeto)
Excluir ou editar URLs encurtadas.
Adicionar autenticação para usuários.
Monitorar acessos às URLs encurtadas.
Estabelecer prazos de validade para os links encurtados.
📝 Licença
Este projeto está sob a licença MIT. Isso significa que você pode utilizá-lo, modificá-lo
