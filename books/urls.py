"""
Arquivo de configuração de URLs para o aplicativo de livros.

Módulos:
    - path: Módulo utilizado para definir padrões de URL.
    - views: Módulo contendo as views relacionadas ao aplicativo de livros.

Padrões de URL:
    - books/: Rota para a view que lida com a listagem e criação de livros.
    - book/<int:isbn>/: Rota para a view que lida com os detalhes de um livro
    específico.
"""

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
