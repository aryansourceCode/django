from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

# Display all students
def home(request):
    students = Student.objects.all()
    return render(request, "home.html", {'students': students})

# Add a new student
def stdadd(request):
    if request.method == "POST":
        std_roll = request.POST.get('roll')
        std_name = request.POST.get('name')
        std_email = request.POST.get('email')
        std_phone = request.POST.get('phone')
        std_dob = request.POST.get('dob')
        std_address = request.POST.get('address')
        
        # Create and save the Student instance
        s = Student(
            roll=std_roll,
            name=std_name,
            email=std_email,
            phone=std_phone,
            dob=std_dob,
            address=std_address
        )
        s.save()
        
       
        return redirect('home')

    return render(request, "stdadd.html", {})

# Update an existing student
def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST" and request.POST.get('_method') == 'PUT':
        student.roll = request.POST.get('roll')
        student.name = request.POST.get('name')
        student.email = request.POST.get('email')
        student.phone = request.POST.get('phone')
        student.dob = request.POST.get('dob')
        student.address = request.POST.get('address')
        student.save()
        return redirect('home')
    return render(request, "stdadd.html", {'student': student})

# Delete an existing student
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('home')
