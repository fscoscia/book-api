from django.db import models
from django.utils.translation import gettext_lazy as _


class Author(models.Model):
    first_name = models.CharField(max_length=100, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=100, verbose_name=_("Last Name"))
    bio = models.TextField(blank=True, default="", verbose_name=_("Biography"))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("Title"))
    isbn = models.CharField(max_length=13, unique=True, verbose_name=_("ISBN"))
    publication_date = models.DateField(
        null=True, blank=True, verbose_name=_("Publication Date")
    )
    cover_image = models.ImageField(
        upload_to="book_covers/", null=True, blank=True, verbose_name=_("Cover Image")
    )
    authors = models.ManyToManyField(
        to=Author, verbose_name=_("Authors"), related_name="books"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")

    def __str__(self):
        return f"{self.title}"
