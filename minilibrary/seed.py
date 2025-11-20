"""
How to run this seed script:

Recommended (loads Django context):
    uv run python manage.py shell < minilibrary/seed.py

Or, inside Django shell:
    exec(open('minilibrary/seed.py').read())

Do NOT run directly with 'python minilibrary/seed.py' (will not work outside Django context).
"""

from minilibrary.models import Book, Author
from datetime import date

authors = [
    Author(name="George Orwell", birth_date=date(1903, 6, 25)),
    Author(name="Jane Austen", birth_date=date(1775, 12, 16)),
    Author(name="J.K. Rowling", birth_date=date(1965, 7, 31)),
    Author(name="Gabriel García Márquez", birth_date=date(1927, 3, 6)),
    Author(name="Chinua Achebe", birth_date=date(1930, 11, 16)),
    Author(name="Harper Lee", birth_date=date(1926, 4, 28)),
    Author(name="F. Scott Fitzgerald", birth_date=date(1896, 9, 24)),
    Author(name="Leo Tolstoy", birth_date=date(1828, 9, 9)),
]
Author.objects.bulk_create(authors, ignore_conflicts=True)

authors_db = {a.name: a for a in Author.objects.all()}

books = [
    Book(
        title="1984",
        publication_date=date(1949, 6, 8),
        author=authors_db["George Orwell"],
        pages=328,
        isbn="9780451524935",
    ),
    Book(
        title="Animal Farm",
        publication_date=date(1945, 8, 17),
        author=authors_db["George Orwell"],
        pages=112,
        isbn="9780451526342",
    ),
    Book(
        title="Pride and Prejudice",
        publication_date=date(1813, 1, 28),
        author=authors_db["Jane Austen"],
        pages=279,
        isbn="9780141439518",
    ),
    Book(
        title="Harry Potter and the Philosopher's Stone",
        publication_date=date(1997, 6, 26),
        author=authors_db["J.K. Rowling"],
        pages=223,
        isbn="9780747532699",
    ),
    Book(
        title="Harry Potter and the Chamber of Secrets",
        publication_date=date(1998, 7, 2),
        author=authors_db["J.K. Rowling"],
        pages=251,
        isbn="9780747538493",
    ),
    Book(
        title="One Hundred Years of Solitude",
        publication_date=date(1967, 5, 30),
        author=authors_db["Gabriel García Márquez"],
        pages=417,
        isbn="9780060883287",
    ),
    Book(
        title="Things Fall Apart",
        publication_date=date(1958, 6, 17),
        author=authors_db["Chinua Achebe"],
        pages=209,
        isbn="9780385474542",
    ),
    Book(
        title="To Kill a Mockingbird",
        publication_date=date(1960, 7, 11),
        author=authors_db["Harper Lee"],
        pages=281,
        isbn="9780061120084",
    ),
    Book(
        title="The Great Gatsby",
        publication_date=date(1925, 4, 10),
        author=authors_db["F. Scott Fitzgerald"],
        pages=180,
        isbn="9780743273565",
    ),
    Book(
        title="War and Peace",
        publication_date=date(1869, 1, 1),
        author=authors_db["Leo Tolstoy"],
        pages=1225,
        isbn="9780199232765",
    ),
]
Book.objects.bulk_create(books, ignore_conflicts=True)

print("Seeding completed successfully!")
