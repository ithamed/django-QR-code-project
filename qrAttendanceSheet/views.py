from django.shortcuts import render
from qrAttendanceSheet.models import Course_session, Student_presence
# from qrAttendanceSheet.models import Website, Student
from django.contrib.auth.models import User
from qrAttendanceSheet.forms import Student_presenceForm
from django.http import HttpResponse, HttpResponseRedirect


def home_view(request):
    # name = "Welcome to"
    
    sessions = Course_session.objects.all()
    # objs = Website.objects.all()


    context = {
        'sessions' : sessions,
    }
    return render(request, 'qrAttendanceSheet/home.html', context)

def register(request, session_id):
    current_user = request.user
    user = {
        'current_user' : current_user,
        'obj' : session_id,
    }
    if request.POST:
        course_session = Course_session.objects.get(id=session_id)
        # print(" %%%%%%%%%%   ", course_session)
        try:
            student = Student_presence(course_session= course_session, student = request.user)
            student.save()
            return render(request, 'qrAttendanceSheet/registered.html', user)
        except:
            # later a proper message or page should come instead
            return HttpResponse("you are already registered")
            
    else:
        # print(request.body)
        return render(request, 'qrAttendanceSheet/register.html', user)


#renders all records from Student_presence from specific session
def student(request, session_id): 
    students = Student_presence.objects.filter(course_session=session_id)
    session = Course_session.objects.get(id=session_id) 
    std = {
        'students' : students,
        'session': session
    }
    print("ine?",students)

    return render(request, 'qrAttendanceSheet/students.html', std)