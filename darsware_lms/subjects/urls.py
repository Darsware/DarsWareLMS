from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # /subjects/
    path("<str:subject>", views.subject_description, name="subject_description"),  # /subjects/math
]




