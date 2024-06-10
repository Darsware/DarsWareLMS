from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse


# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)

    # Modify & overwrite get_absolute_url method
    def get_absolute_url(self):
        return reverse("book-detail", args=[str(self.id)])

    # Remember:
    # The reverse function is a powerful tool in Django for generating URLs dynamically. 
    # It allows you to create URLs based on the names of your views and the arguments they need. 
    # This makes your code more readable, maintainable, and less prone to errors.




    def __str__(self):
        return f"{self.title} ({self.rating}) by {self.author}"
