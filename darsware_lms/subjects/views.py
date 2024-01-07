from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


subjects_dict = {
    "math": "Welcome to Math courses page",
    "science": "Welcome to Science courses page",
    "ict": "Welcome to ICT courses page",
    "english": None,
}


# Create your views here.


def index(request):
    subjects = list(subjects_dict.keys())
    return render(request, "subjects/index.html", {
            "subjects": subjects,
    },)


def subject_description(request, subject):
    subject = str(subject).lower()  # convert to lowercase
    try:
        subject_text = subjects_dict[subject]
        return render(request, "subjects/subject.html", {
            "text": subject_text,
            "subject_name": subject,
        })
    except KeyError:
        return HttpResponseNotFound("This Subject not found")