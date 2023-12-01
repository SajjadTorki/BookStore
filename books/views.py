from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import Book
from .forms import BookForm, CommentForm
from django.shortcuts import get_object_or_404


# Create your views here.


class BookListView(generic.ListView):
    model = Book
    paginate_by = 4
    template_name = "book/book_list.html"
    context_object_name = 'books'


# class BookDetailView(generic.DetailView):
#     model = Book
#     template_name = 'book/book_detail.html'
#     context_object_name = 'book'


def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book_comment = book.comments.all()
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    context = {
        'book': book,
        'comments': book_comment,
        'comment_form': comment_form,
    }
    return render(request, 'book/book_detail.html', context)


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
