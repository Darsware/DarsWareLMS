# students/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # Example path
    # Add other paths here
]