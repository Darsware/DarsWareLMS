from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="starting-page"),
    path("<int:id>", views.book_detail, name="book-detail")
]
