from ninja import NinjaAPI, Schema
import datetime
from minilibrary.models import Author, Book

api = NinjaAPI()


class AuthorSchema(Schema):
    id: int
    name: str
    birth_date: datetime.date | None


class BookSchema(Schema):
    id: int
    title: str
    publication_date: datetime.date | None
    author_id: int
    pages: int
    isbn: str


@api.get("/authors", response=list[AuthorSchema])
def list_authors(request):
    return Author.objects.all()


@api.get("/books", response=list[BookSchema])
def list_books(request):
    return Book.objects.all()
