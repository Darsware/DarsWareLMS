from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.
def get_date(post):
    return post.date

def starting_page(request):
    # Get all posts and order them by date in descending order ( -date)[:3] is slicing
    all_posts = Post.objects.all()
    latest_posts = Post.objects.all().order_by("-date")[:3]
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/blog.html", {"posts": latest_posts})


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {"all_posts": all_posts})


def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    # Find next element that matches a certain condition
    # The next() function returns the next item in an iterator.
    return render(request, "blog/post-detail.html", {
        "post": identified_post,
        "post_tags": identified_post.tags.all(),
        })
