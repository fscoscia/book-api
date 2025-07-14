from django.core.management.base import BaseCommand
from core.models import Author, Book


class Command(BaseCommand):
    help = "Populate authors and books initial data"

    def handle(self, *args, **options):
        author1 = Author.objects.create(
            first_name="Gabriel", last_name="García Márquez", bio="Escritor colombiano."
        )
        author2 = Author.objects.create(
            first_name="Isabel", last_name="Allende", bio="Escritora chilena."
        )

        book1 = Book.objects.create(
            title="Cien años de soledad",
            isbn="12121212",
            publication_date="1967-06-05",
        )
        book1.authors.add(author1)

        book2 = Book.objects.create(
            title="La casa de los espíritus",
            isbn="1313131313",
            publication_date="1982-01-01",
        )
        book2.authors.add(author2)

        book3 = Book.objects.create(
            title="Libro con 2 autores",
            isbn="1414141414",
            publication_date="1970-01-01",
        )
        book3.authors.add(author1, author2)

        self.stdout.write(self.style.SUCCESS("Datos iniciales cargados correctamente"))
