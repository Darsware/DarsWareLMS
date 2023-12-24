from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # /courses/
    path("<str:subject>", views.subject, name="subject"),  # /courses/math/
]
