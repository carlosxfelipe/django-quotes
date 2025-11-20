## Django Quotes

Este projeto é uma aplicação Django para gerenciar e exibir citações.

### Pré-requisitos

- [Python](https://www.python.org/) instalado
- [uv](https://github.com/charliermarsh/uv) instalado para executar comandos

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

O app `quotes` foi criado com o comando:

```bash
uv run python manage.py startapp quotes
```

O app `landing` foi criado com o comando:

```bash
uv run python manage.py startapp landing
```

O app `minilibrary` foi criado com o comando:

```bash
uv run python manage.py startapp minilibrary
```

```bash
uv run python manage.py makemigrations
```

```bash
uv run python manage.py showmigrations
```

```bash
uv run python manage.py migrate
```

Consulte a documentação do Django para mais comandos e opções.
