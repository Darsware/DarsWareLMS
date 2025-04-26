from django.contrib import admin
from .models import Post, Author, Tag

# Register your models here.


# Create class admin that extends admin.ModelAdmin
class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date",) # values in tuple should have the same name as the fields in the model
    list_display= ("title", "date", "author",)
    prepopulated_fields = {"slug": ("title",)} # Automatically populate the slug field based on the title field

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)