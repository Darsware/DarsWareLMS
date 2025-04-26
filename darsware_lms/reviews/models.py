from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Review(models.Model):
    """This class creates a model for the review page."""

    user_name = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=100)
    user_review = models.TextField(max_length=250)
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1, message="Rating must be at least 1."),
            MaxValueValidator(5, message="Rating cannot exceed 5.")
    ])

    def __str__(self):
        return self.user_name

