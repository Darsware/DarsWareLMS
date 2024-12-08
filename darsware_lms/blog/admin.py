from django.contrib import admin
from .models import Post, Author, Tag

# Register your models here.


# Create class admin that extends admin.ModelAdmin
class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date",)
    list_display= ("title", "author", "date",)

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)