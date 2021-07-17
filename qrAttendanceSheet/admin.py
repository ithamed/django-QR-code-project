from django.contrib import admin
from .models import Course_session, Student_presence
# Register your models here.

admin.site.register(Course_session)
admin.site.register(Student_presence)
