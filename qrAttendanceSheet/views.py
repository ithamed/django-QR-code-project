from django.shortcuts import render
from qrAttendanceSheet.models import Course_session, Student_presence
# from qrAttendanceSheet.models import Website, Student
from django.contrib.auth.models import User
from qrAttendanceSheet.forms import Student_presenceForm

def home_view(request):
    # name = "Welcome to"

    sessions = Course_session.objects.all()
    # objs = Website.objects.all()


    context = {
        'sessions' : sessions,
    }
    

    return render(request, 'home.html', context)

def register(request, session_id):
    current_user = request.user
    user = {
        'current_user' : current_user,
        'obj' : session_id,
    }
    if request.POST:
        course_session = Course_session.objects.get(id=session_id)
        # print(" %%%%%%%%%%   ", course_session)
        student = Student_presence(course_session= course_session, student = request.user)
        student.save()
        return render(request, 'registered.html', user)
    else:
        print(request.body)
        return render(request, 'register.html', user)


#renders all records from Student_presence from specific session
def student(request, session_id): 
    students = Student_presence.objects.filter(course_session=session_id) 
    std = {
        'students' : students,
    }
    print(students)

    return render(request, 'students.html', std)