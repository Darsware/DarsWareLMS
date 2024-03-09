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
        "content": """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s. When an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
        
            It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.""",
    },
    {
        "slug": "my-second-post",
        "image": "darsware.jpeg",
        "author": "Darsware Member",
        "date": date(2024, 3, 10),
        "title": "My second post",
        "excerpt": "This is my second post with more content inside",
        "content": """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s. When an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
        
            It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.""",
    },
    {
        "slug": "my-third-post",
        "image": "darsware.jpeg",
        "author": "Darsware Staff",
        "date": date(2024, 4, 10),
        "title": "My third post",
        "excerpt": "This is my third post with more content inside",
        "content": """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s. When an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
        
            It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.""",
    },
]


# Create your views here.


def get_date(post):
    return post["date"]


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/blog.html", {"posts": latest_posts})


def posts(request):
    return render(request, "blog/all-posts.html", {"all_posts": all_posts})


def post_detail(request, slug):
    # Find next element that matches a certain condition
    # The next() function returns the next item in an iterator.
    identified_post = next(post for post in all_posts if post["slug"] == slug)
    return render(request, "blog/post-detail.html", {"post": identified_post})
