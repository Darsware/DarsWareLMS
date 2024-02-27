from django.shortcuts import render
from datetime import date



all_posts = [
    {
        "slug": "my-first-post",
        "image": "darsware_logo.png",
        "author": "Mentash",
        "date": date(2024, 2, 10),
        "title": "My first post",
        "excerpt": "This is my first post with more content inside",
        "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
    },
    {
        "slug": "my-second-post",
        "image": "darsware.jpeg",
        "author": "Darsware Member",
        "date": date(2024, 3, 10),
        "title": "My second post",
        "excerpt": "This is my second post with more content inside",
        "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
    },
    {
        "slug": "my-third-post",
        "image": "darsware.jpeg",
        "author": "Darsware Staff",
        "date": date(2024, 4, 10),
        "title": "My third post",
        "excerpt": "This is my third post with more content inside",
        "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
    }
]


# Create your views here.

def get_date(post):
    return post['date']


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/blog.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })




def post_detail(request, slug):
    return render(request, "blog/post-detail.html")

