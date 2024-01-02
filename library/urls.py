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
