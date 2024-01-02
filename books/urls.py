from django.urls import path
from books import views

urlpatterns = [
    path(
        'books/',
        views.BookListCreateView.as_view(),
        name='books-list'
    ),

    path(
        'book/<int:isbn>/',
        views.BookDetailView.as_view(),
        name='book-detail'
    )
]
