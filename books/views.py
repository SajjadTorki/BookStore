from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import Book
from .forms import BookForm


# Create your views here.


class BookListView(generic.ListView):
    model = Book
    template_name = "book/book_list.html"
    context_object_name = 'books'


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book/book_detail.html'
    context_object_name = 'book'


class BookCreateView(generic.CreateView):
    model = Book
    fields = ['title', 'author', 'description', 'price', 'cover']
    template_name = "book/book_new.html"
    success_url = reverse_lazy('book_list')


class BookEditView(generic.UpdateView):
    form_class = BookForm
    model = Book

    template_name = "book/book_new.html"
    success_url = reverse_lazy('book_list')


class BookDeletView(generic.DeleteView):
    model = Book
    context_object_name = 'book'
    template_name = "book/book_delete.html"
    success_url = reverse_lazy('book_list')
