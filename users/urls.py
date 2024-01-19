"""
Arquivo de configuração de URLs para a app de users.

Módulos:
    - path: Módulo utilizado para definir padrões de URL.
    - views: Módulo contendo as views relacionadas a app de users.

Padrões de URL:
    - users/: Rota para a view que lida com a listagem e criação de contas
    para os usuários.
    - user/<str:username>/: Rota para a view que lida com os detalhes de uma
    conta de usuário específica.
"""

from django.urls import path
from users import views

urlpatterns = [
    path(
        'users/',
        views.UserListCreateAPIView.as_view(),
        name='users-list'
    ),

    path(
        'user/<str:username>/',
        views.UserDetailView.as_view(),
        name='user-detail'
    )
]
