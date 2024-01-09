from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse


subjects = {
    "math": "Welcome to Math courses page",
    "science": "Welcome to Science courses page",
    "ict": "Welcome to ICT courses page",
}

stages = {
    "primary": "Welcome to Primary stage courses page",
    "preparatory": "Welcome to Preparatory stage courses page",
    "secondary": "Welcome to Secondary stage courses page",
}

courses = {
    # iterate stages and subjects to Create stage_subject prefix before course name using dictionary comprehension
    f"{stage}_{subject}": f"Welcome to {stage} {subject} courses page" for stage in stages for subject in subjects
}

print(courses)


# Create your views here.


# Create index view function
def index(request):
    courses_list = list(courses.keys())
    return render(request, "courses/index.html", {
        "subjects": subjects,
        "stages": stages,
        "courses": courses_list,
    })


def course_description(request, course):
    course = str(course).lower()  # convert to lowercase
    try:
        course_text = courses[course]
        return render(request, "courses/course.html", {
            "text": course_text,
            "course_name": course,
        })
    except KeyError:
        return HttpResponseNotFound(f"Course '{course}' not found. Please enter a valid course.")


# def subject_description(request, subject):
#     subject = str(subject).lower()  # convert to lowercase
#     try:
#         subject_text = subjects[subject]
#         return render(request, "courses/subject.html", {
#             "text": subject_text,
#             "subject_name": subject,
#         })
#     except KeyError:
#         return HttpResponseNotFound("This Subject not found")
