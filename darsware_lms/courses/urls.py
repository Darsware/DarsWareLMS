from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # /courses/
    # path("<str:subject>", views.subject_description, name="subject_description"),  # /courses/math/
    path("<str:course>", views.course_description, name="course_description"),  # /courses/primary_math/
]
