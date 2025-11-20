# Comandos do Django Shell para criar autores e livros

```python
from minilibrary.models import Author, Book

# Criando autores
a1 = Author.objects.create(name="Jorge Amado", birth_date="1912-08-10")
a2 = Author.objects.create(name="Clarice Lispector", birth_date="1920-12-10")
a3 = Author.objects.create(name="Machado de Assis", birth_date="1839-06-21")

# Criando livros

# Jorge Amado
Book.objects.create(
    title="Capitães da Areia",
    publication_date="1937-01-01",
    pages=280,
    isbn="9781234567890",
    author=a1
)

Book.objects.create(
    title="Gabriela, Cravo e Canela",
    publication_date="1958-01-01",
    pages=400,
    isbn="9789876543210",
    author=a1
)

# Clarice Lispector
Book.objects.create(
    title="A Hora da Estrela",
    publication_date="1977-01-01",
    pages=96,
    isbn="9781111111111",
    author=a2
)

# Machado de Assis
Book.objects.create(
    title="Dom Casmurro",
    publication_date="1899-01-01",
    pages=256,
    isbn="9782222222222",
    author=a3
)

Book.objects.create(
    title="Memórias Póstumas de Brás Cubas",
    publication_date="1881-01-01",
    pages=240,
    isbn="9783333333333",
    author=a3
)
