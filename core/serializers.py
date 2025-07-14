from rest_framework import serializers
from core.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "first_name", "last_name", "bio"]


class BookSerializer(serializers.ModelSerializer):
    # Serialize the relation with authors using AuthorSerializer
    # Just for list operation
    authors = AuthorSerializer(many=True, read_only=True)
    # Just for the create/update operations
    author_ids = serializers.PrimaryKeyRelatedField(
        many=True, write_only=True, queryset=Author.objects.all(), source="authors"
    )
    authors_qty = serializers.IntegerField(read_only=True)

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "isbn",
            "publication_date",
            "cover_image",
            "authors",
            "authors_qty",
            "author_ids",
        ]
