from django.shortcuts import render
from websites.models import Website, Student
from django.contrib.auth.models import User
from websites.forms import StudentForm

def home_view(request):
    # name = "Welcome to"

    objs = Website.objects.all()


    context = {
        # 'name': name,
        'objs' : objs,
    }
    

    return render(request, 'home.html', context)

def register(request, obj):
    current_user = request.user
    user = {
        'current_user' : current_user,
        'obj' : obj,
    }
    if request.POST:
        website = Website.objects.get(id=obj)
        student = Student(website= website, student = request.user)
        student.save()
        return render(request, 'registered.html', user)
    else:
        print(request.body)
        return render(request, 'register.html', user)

def student(request):
    students = Student.objects.all()
    std = {
        'students' : students,
    }
    print(students)

    return render(request, 'students.html', std)