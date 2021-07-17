from django.urls import path
from .views import home_view, register, student

urlpatterns = [
    path('', home_view, name='home'),
    path('register/<int:session_id>', register, name='register'),
    path('list/session/<int:session_id>', student, name='list'), #list of students that attended to the class
]