from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Student

def student_list(request):
    """Display all students"""
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def student_detail(request, pk):
    """Display a single student's details"""
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})

def student_create(request):
    """Create a new student"""
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        gpa = request.POST.get('gpa')
        
        try:
            Student.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                gpa=gpa or 0.0
            )
            messages.success(request, 'Student created successfully!')
            return redirect('student_list')
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
    
    return render(request, 'students/student_form.html')

def student_update(request, pk):
    """Update a student's information"""
    student = get_object_or_404(Student, pk=pk)
    
    if request.method == 'POST':
        student.first_name = request.POST.get('first_name')
        student.last_name = request.POST.get('last_name')
        student.email = request.POST.get('email')
        student.phone = request.POST.get('phone')
        student.gpa = request.POST.get('gpa')
        
        try:
            student.save()
            messages.success(request, 'Student updated successfully!')
            return redirect('student_detail', pk=pk)
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
    
    return render(request, 'students/student_form.html', {'student': student})

def student_delete(request, pk):
    """Delete a student"""
    student = get_object_or_404(Student, pk=pk)
    
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student deleted successfully!')
        return redirect('student_list')
    
    return render(request, 'students/student_confirm_delete.html', {'student': student})
