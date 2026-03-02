from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'gpa', 'enrollment_date']
    list_filter = ['enrollment_date', 'gpa']
    search_fields = ['first_name', 'last_name', 'email']
    ordering = ['last_name', 'first_name']
