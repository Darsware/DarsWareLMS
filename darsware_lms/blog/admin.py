from django.contrib import admin
from .models import Post, Author, Tag

# Register your models here.


# Create class admin that extends admin.ModelAdmin



admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Tag)


