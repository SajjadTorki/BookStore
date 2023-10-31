from django.urls import path
from .views import *

urlpatterns = [
    path("booklist/", BookListView.as_view(), name='book_list'),
    path('bookdetail<int:pk>', BookDetailView.as_view(), name='book_detail'),
    path('bookcreate', BookCreateView.as_view(), name='book_create'),
    path('bookupdate/<int:pk>/', BookEditView.as_view(), name="book_update"),
    path('bookdelete/<int:pk>/', BookDeletView.as_view(), name="book_delete"),

]
