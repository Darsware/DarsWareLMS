from django.shortcuts import get_object_or_404,render
from django.http import Http404


# Import Book class from models
from .models import Book

# Create your views here.


def index(request):
    books = Book.objects.all()
    return render(request, "books/index.html", {
        "books": books
    })

def book_detail(request, id):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()
    book = get_object_or_404(Book, pk=id)
    return render(request, "books/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller": book.is_bestselling
    })