# URL Shortener 🔗

Este é um projeto simples de encurtador de URLs desenvolvido com as seguintes tecnologias:

- **Frontend:** HTML, CSS e JavaScript
- **Backend:** Python (Flask)
- **Banco de Dados:** SQLite

### 📋 Funcionalidades

- Encurtar URLs longas.
- Redirecionar URLs encurtadas para o endereço original.
- Interface simples e amigável.

---

## 🚀 Como rodar o projeto

Siga as instruções abaixo para configurar e executar o projeto localmente.

### Pré-requisitos

Você precisará ter instalado:

- Python 3.7 ou superior
- Um navegador atualizado

### Passo a passo

1. **Clone este repositório**:
   ```bash
   git clone https://github.com/seu-usuario/url-shortener.git
   cd url-shortener
   ```

2. **Crie um ambiente virtual**:
   ```bash
   python -m venv venv
   ```

3. **Ative o ambiente virtual**:

   - No Linux/macOS:
     ```bash
     source venv/bin/activate
     ```
   - No Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Instale as dependências**:
   ```bash
   pip install flask
   ```

5. **Execute o aplicativo**:
   ```bash
   python app.py
   ```

6. **Acesse no navegador**:
   Abra o navegador e entre no endereço: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 📂 Estrutura do Projeto

```plaintext
url-shortener/
├── static/
│   ├── style.css       # Estilização da aplicação
│   ├── script.js       # JavaScript do frontend
├── templates/
│   ├── index.html      # Página principal do sistema
├── app.py              # Backend com Flask
├── database.db         # Banco de dados SQLite
├── README.md           # Documentação do projeto
```

---

## 📚 Tecnologias Utilizadas

- **Flask**: Framework Python para web.
- **HTML**: Estrutura da página.
- **CSS**: Estilização customizada.
- **JavaScript**: Comunicação com o servidor através de requisições assíncronas.
- **SQLite**: Banco de dados local.

---

## ✨ Funcionalidades Futuras (Se desejar melhorar o projeto)

- Excluir ou editar URLs encurtadas.
- Adicionar autenticação para usuários.
- Monitorar acessos às URLs encurtadas.
- Estabelecer prazos de validade para os links encurtados.

---

## 📝 Licença

Este projeto está sob a licença **MIT**. Isso significa que você pode utilizá-lo, modificá-lo