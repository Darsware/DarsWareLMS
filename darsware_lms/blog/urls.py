from django.urls import path
# import views
from . import views

urlpatterns = [
    path("", views.starting_page, name="stating-page"),  # /blog/
    path("posts", views.posts, name="posts-page"),  # /blog/posts/
    path("posts/<slug:slug>", views.post_detail, name="post-detail-page")  # /blog/posts/my-first-post/
]

