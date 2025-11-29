## Django Quotes

Este projeto é uma aplicação Django para gerenciar e exibir citações.

### Como rodar após clonar
1. Instale o gerenciador de pacotes `uv` (se não tiver):
  - **macOS e Linux:**
    ```zsh
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```
  - **Windows:**
    ```powershell
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```
2. Instale as dependências do projeto e configure tudo automaticamente:
  ```zsh
  uv run setup.py
  ```
3. Acesse no navegador:
  - Quotes: http://localhost:8000/quotes/
  - Landing: http://localhost:8000/landing/home

### Como adicionar um novo app

Para adicionar um novo app Django ao projeto, siga os passos abaixo:

1. Crie o app substituindo `nome` pelo nome desejado:
  ```bash
  uv run python manage.py startapp nome
  ```

2. Adicione o app criado à lista `INSTALLED_APPS` em `config/settings.py` para ativá-lo no projeto.

3. (Opcional) Crie as rotas do app em `nome/urls.py` e inclua-as no arquivo principal de rotas (`config/urls.py`).

4. (Opcional) Crie modelos, views e templates conforme necessário para o seu app.

Consulte a [documentação oficial do Django](https://docs.djangoproject.com/pt-br/4.2/intro/tutorial01/) para mais detalhes e boas práticas.

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
