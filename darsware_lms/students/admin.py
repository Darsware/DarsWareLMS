from django.contrib import admin
from .models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone_number", "address", "city", "governorate", "country",)


admin.site.register(Student, StudentAdmin)


