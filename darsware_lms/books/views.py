from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.db.models import Avg


# Import Book class from models
from .models import Book

# Create your views here.


def index(request,):
    # Get all books and order them by title. ( -title) is descending order
    # OR Get all books and order them by rating. ( -rating) is descending order
    books = Book.objects.all().order_by("-title")
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))  # Returns a dictionary. So, use keys to access values

    return render(request, "books/index.html", {
        "books": books,
        "total_number_of_books": num_books,
        "average_rating": avg_rating
    })


def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()
    book = get_object_or_404(Book, slug=slug)
    return render(request, "books/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller": book.is_bestselling
    })