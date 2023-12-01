from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import Book
from .forms import BookForm
from django.shortcuts import get_object_or_404


# Create your views here.


class BookListView(generic.ListView):
    model = Book
    paginate_by = 4
    template_name = "book/book_list.html"
    context_object_name = 'books'


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book/book_detail.html'
    context_object_name = 'book'


def book_detail_view(request, pk):
    books = get_object_or_404(Book, pk=pk)
    book_comment = books.comments.all()

    return render(request, 'book/book_detail.html', {'book': books, 'comments': book_comment})


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
