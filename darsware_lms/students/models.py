from django.db import models

# Create your models here.


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=50)
    governorate = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

    class Meta:
        verbose_name_plural = "Students"




