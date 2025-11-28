## Django Quotes

Este projeto é uma aplicação Django para gerenciar e exibir citações.

### Como rodar após clonar
1. Instale o gerenciador de pacotes `uv` (se não tiver):
  ```zsh
  pip install uv
  # ou, alternativamente:
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```
2. Instale as dependências do projeto e configure tudo automaticamente:
  ```zsh
  uv run setup.py
  ```
3. Acesse no navegador:
  - Quotes: http://localhost:8000/quotes/
  - Landing: http://localhost:8000/landing/home

### Pré-requisitos

- [Python](https://www.python.org/) instalado
- [uv](https://github.com/charliermarsh/uv) instalado para executar comandos
- **Pacote correto:** [django-ninja](https://django-ninja.dev/) (não instale o pacote chamado apenas 'ninja')

### Como iniciar o projeto

1. **Aplicar as migrações do banco de dados:**

   ```bash
   uv run python manage.py migrate
   ```

2. **Executar o servidor de desenvolvimento:**

   ```bash
   uv run python manage.py runserver
   ```

3. **Acessar a aplicação:**
   - **Quotes App:** http://localhost:8000/quotes/
   - **Landing Page:** http://localhost:8000/landing/home

---

### Histórico

- O app `quotes` foi criado com o comando:
  ```bash
  uv run python manage.py startapp quotes
  ```
  Responsável por exibir e gerenciar citações diárias.

- O app `landing` foi criado com o comando:
  ```bash
  uv run python manage.py startapp landing
  ```
  Responsável pela página inicial e institucional do projeto.

- O app `minilibrary` foi criado com o comando:
  ```bash
  uv run python manage.py startapp minilibrary
  ```
  Gerencia autores e livros, com modelos `Author` e `Book`.

- Comandos de migração utilizados:
  ```bash
  uv run python manage.py makemigrations
  uv run python manage.py showmigrations
  uv run python manage.py migrate
  ```
  Usados para criar e aplicar as migrações do banco de dados.

- Comando para acessar o shell interativo:
  ```bash
  uv run python manage.py shell
  uv run python manage.py shell --interface=ipython
  ```
  Permite executar scripts e interagir com os modelos.

- Script de seed criado em `minilibrary/seed.py` para popular o banco com autores e livros de exemplo usando `bulk_create`.

- Django Admin disponível em `/admin/` para gerenciar todos os registros, acessível após criar um superusuário com:
  ```bash
  uv run python manage.py createsuperuser
  ```

### Como adicionar dependências com uv

Para instalar um pacote e registrar automaticamente nas dependências do projeto (pyproject.toml), use o comando:

```zsh
uv add django-ninja
```
Esse é o comando certo para instalar o pacote com uv e garantir que ele seja incluído nas dependências do projeto.

---

### API REST com Django Ninja

Este projeto utiliza [Django Ninja](https://django-ninja.dev/) para criar rotas REST no app `minilibrary`:

- `GET /minilibrary/api/authors` — Lista todos os autores cadastrados
- `GET /minilibrary/api/books` — Lista todos os livros cadastrados
- `GET /minilibrary/api/docs` — Documentação interativa Swagger da API

As rotas retornam dados em formato JSON e podem ser acessadas diretamente pelo navegador, curl ou ferramentas como Postman. A documentação Swagger permite testar e explorar a API de forma visual.

Consulte a documentação do Django para mais comandos e opções.
