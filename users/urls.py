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
