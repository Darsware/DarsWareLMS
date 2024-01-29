from django.urls import path
from .views import starting_page, posts, post_detail

urlpatterns = [
    path("", starting_page, name="stating-page"),  # /blog/
    path("blog/posts", posts, name="posts-page"),  # /blog/posts/
    path("posts/<slug:slug>", post_detail, name="post-detail-page")  # /blog/posts/my-first-post/
]

