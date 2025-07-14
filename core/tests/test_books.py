import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from core.models import Author, Book


@pytest.mark.django_db
def test_create_book():
    # Test to verify that the book is create correctly
    author1 = Author.objects.create(first_name="Nombre 1", last_name="Apellido 1")
    author2 = Author.objects.create(first_name="Nombre 2", last_name="Apellido 2")

    client = APIClient()
    data = {
        "title": "Libro",
        "isbn": "111111111",
        "publication_date": "2025-07-13",
        "author_ids": [author1.id, author2.id],
    }
    response = client.post("/books/", data)

    assert response.status_code == 201
    assert Book.objects.count() == 1
    assert Book.objects.first().authors.count() == 2


@pytest.mark.django_db
def test_get_book():
    # Test to verify that get the book correctly
    author = Author.objects.create(first_name="Nombre 1", last_name="Apellido 1")
    book = Book.objects.create(
        title="Titulo", isbn="111111111", publication_date="2025-07-13"
    )
    book.authors.add(author)

    client = APIClient()
    response = client.get(f"/books/{book.id}/")

    assert response.status_code == 200
    assert response.data["title"] == "Titulo"
