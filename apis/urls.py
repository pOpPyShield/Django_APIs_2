from django.contrib import admin
from django.urls import path, include
from .views import BookAPIView

urlpatterns = [
    path("books/", BookAPIView.as_view(), name="book_list"),
    path("todos/", include("todos.urls")),
]
