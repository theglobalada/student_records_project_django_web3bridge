from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11, blank=True)
    enrollment_date = models.DateField(auto_now_add=True)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        ordering = ['last_name', 'first_name']
