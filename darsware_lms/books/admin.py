from django.contrib import admin

from .models import Book

# Register your models here.

# Create class admin that extends admin.ModelAdmin
# Allows to customize the admin panel for the Book model and set options
# Can overwrite methods and add custom methods of extended class
class BookAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)} # Automatically populate the slug field based on the title field



# Make django aware of models and register them
admin.site.register(Book, BookAdmin)

