from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
#from django.utils.text import slugify  # Transforms a string to a slug


# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=2)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Countries"


class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}, {self.postal_code} {self.city}"

    class Meta:
        verbose_name_plural = "Address Entries"



class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True, blank=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    

    def __str__(self):
        return self.full_name()
    

class Publisher(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="books")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True, related_name="books")
    published_countries = models.ManyToManyField(Country, null=False)
    is_bestselling = models.BooleanField(default=False)
    # Add a slug field to the Book model
    slug = models.SlugField(default="", 
                            blank=True, # Allow empty values
                            # editable=False, # Don't allow editing in the admin panel and hide it
                            null=False, 
                            db_index=True)  # /books/123 -> /books/harry-potter-1

    # Modify & overwrite get_absolute_url method
    def get_absolute_url(self):
        return reverse("book-detail", args=[str(self.slug)])

    # Remember:
    # The reverse function is a powerful tool in Django for generating URLs dynamically. 
    # It allows you to create URLs based on the names of your views and the arguments they need. 
    # This makes your code more readable, maintainable, and less prone to errors.

    # # Overwrite the save method
    # def save(self, *args, **kwargs):
    #     # Convert title (string) to a slug
    #     # Set slug to value based on title
    #     # To make sure that a value other than the default "" slug value default="" is added to the slug field
    #     self.slug = slugify(self.title)  # Ex. "Harry Potter 1" -> "harry-potter-1"
    #     # Call the parent's save() method
    #     super().save(*args, **kwargs)

    def __str__(self):
        # Return a string representation of the
        # It will be used in the Django admin
        return f"{self.title} by {self.author} ({self.rating})"
