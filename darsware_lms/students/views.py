from django.shortcuts import render

# Create your views here.

# Import the Student model
from .models import Student


# Create a function for the index page
def index(request):
    return render(request, "students/index.html")




# Create a function that returns a list of students
def student_list(request):
    students = Student.objects.all()
    return render(request, "students/student_list.html", {
        "students": students
    })
