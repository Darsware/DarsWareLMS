from django.contrib import admin

from .models import Book, Author

# Register your models here.

# Create class admin that extends admin.ModelAdmin
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name",)






# Create class admin that extends admin.ModelAdmin
# Allows to customize the admin panel for the Book model and set options
# Can overwrite methods and add custom methods of extended class
# The ModelAdmin class is the representation of a model in the admin interface
class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",) # You need to remove this for the prepopulated_fields to work
    prepopulated_fields = {"slug": ("title",)} # Automatically populate the slug field based on the title field
    list_filter = ("author", "rating",) # Add filters to the right side of the admin panel
    list_display = ("title", "author", "rating",) # Display these fields in the admin panel



# Make django aware of models and register them
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)