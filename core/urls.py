from rest_framework.routers import DefaultRouter
from django.urls import path, include

from core.views import AuthorViewSet, BookViewSet

router = DefaultRouter()
router.register("authors", AuthorViewSet)
router.register("books", BookViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
