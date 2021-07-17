# from django.shortcuts import render
# # from websites.models import Course_session, Student_presence
# from websites.models import Website, Student
# from django.contrib.auth.models import User
# from websites.forms import StudentForm

# def home_view(request):
#     # name = "Welcome to"

#     # objs = Course_session.objects.all()
#     objs = Website.objects.all()


#     context = {
#         'objs' : objs,
#     }
    

#     return render(request, 'home.html', context)

# def register(request, obj):
#     current_user = request.user
#     user = {
#         'current_user' : current_user,
#         'obj' : obj,
#     }
#     if request.POST:
#         # course_session = Course_session.objects.get(id=obj)
#         # student = Student_presence(course_session= course_session, student = request.user)
#         website = Website.objects.get(id=obj)
#         student = Student(website= website, student = request.user)
#         student.save()
#         return render(request, 'registered.html', user)
#     else:
#         print(request.body)
#         return render(request, 'register.html', user)

# def student(request): #in che kar mikone?
#     students = Student.objects.all()
#     std = {
#         'students' : students,
#     }
#     print(students)

#     return render(request, 'students.html', std)