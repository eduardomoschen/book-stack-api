"""
Arquivo de configuração de URLs para o aplicativo de livros.

Módulos:
    - path: Módulo utilizado para definir padrões de URL.
    - views: Módulo contendo as views relacionadas ao aplicativo de livros.

Padrões de URL:
    - borrows/: Rota para a view que lida com a listagem e criação de
    empréstimos de livros.
    - borrow/<int:id>/: Rota para a view que lida com os detalhes de um
    empréstimo específico.
"""

from django.urls import path
from library import views

urlpatterns = [
    path(
        'borrows/',
        views.BookBorrowingCreateListView.as_view(),
        name='borrows-list'
    ),

    path(
        'borrow/<int:id>/',
        views.BookBorrowingDetailView.as_view(),
        name='borrow-detail'
    )
]
