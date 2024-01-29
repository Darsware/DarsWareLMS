from django.shortcuts import render

# Create your views here.


def starting_page(request):
    return render(request, "blog/blog.html")


def posts(request):
    pass


def post_detail(request, slug):
    pass

