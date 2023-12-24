from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

subjects = {
    "math": "Welcome to Math courses page",
    "science": "Welcome to Science courses page",
}

# Create your views here.


# Create index view function
def index(request):
    return HttpResponse("Hello, world. You're at the courses index.")

def subject(request, subject):
    subject = str(subject).lower() # convert to lowercase
    try:
        subject_text = subjects[subject]
        return HttpResponse(subject_text)
    except KeyError:
        return HttpResponseNotFound("Subject not found")

