from django.contrib import admin
from .models import Student
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll', 'name', 'email', 'phone', 'dob', 'address')
    search_fields = ('roll', 'name', 'email')

# Register your models here.
