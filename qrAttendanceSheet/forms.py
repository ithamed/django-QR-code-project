from django.forms import ModelForm
from .models import Student_presence


class Student_presenceForm(ModelForm):

    class Meta:
        model = Student_presence

        fields=['course_session', 'student']        
