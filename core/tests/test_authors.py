import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from core.models import Author


@pytest.mark.django_db
def test_create_author():
    # Test to verify that the author is create correctly
    client = APIClient()
    data = {"first_name": "Nombre", "last_name": "Apellido", "bio": "Biografía"}
    response = client.post("/authors/", data)
    assert response.status_code == 201
    assert Author.objects.count() == 1


@pytest.mark.django_db
def test_get_authors():
    # Test to verify get the book list
    Author.objects.create(first_name="Nombre 1", last_name="Apellido 1")
    Author.objects.create(first_name="Nombre 2", last_name="Apellido 2")

    client = APIClient()
    response = client.get("/authors/")
    assert response.status_code == 200
    assert len(response.data) == 2
