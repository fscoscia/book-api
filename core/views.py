from rest_framework import viewsets
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count


# Viewset to manage the CRUD operations for the Book Model
class BookViewSet(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    search_fields = ["title", "authors__first_name", "authors__last_name"] 
    ordering_fields = ['title',]
    http_method_names = ["get", "post", "put", "delete", "head", "options"]

    def get_queryset(self):
        """
        Function to demonstrate the annotate use, can be resolved by another ways
        Return the queryset with the quantity of authors per book
        """
        return super().get_queryset().annotate(authors_qty=Count("authors"))

    @action(detail=False, methods=["get"])
    def total_books(self, request):
        """
        Function to demonstrate the aggregate use
        Return the total of books in the database
        """
        return Response(self.queryset.aggregate(total=Count("id")))


# Viewset to manage the CRUD operations for the Author Model
class AuthorViewSet(viewsets.ModelViewSet):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    search_fields = ["first_name", "last_name",]
    ordering_fields = ['first_name',"last_name"]
    http_method_names = ["get", "post", "put", "delete", "head", "options"]

    @action(detail=False, methods=["get"])
    def with_books(self, request):
        # Function to count the quantity of books have every author
        data = Author.objects.annotate(book_count=Count("books")).values(
            "id", "first_name", "last_name", "book_count"
        )
        return Response(data)
