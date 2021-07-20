from django.contrib.auth.models import Group, User
from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image

class Course_session(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    date = models.DateField(default='2000-01-01') #should be deleted later


    #this line should be deleted later, and then we can make qr code just when de user asked for that. so we don't save qr in DB and using less storage
    qr_code = models.ImageField(upload_to='qr_codes', blank=True) 



    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    create_at =  models.DateTimeField(auto_now_add=True)
    valid_from =  models.DateTimeField()
    valid_to =  models.DateTimeField()

    def __str__(self):
        return str(self.name) 

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.name)
        canvas = Image.new('RGB', (290, 290), 'white')
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.name}.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)

class Student_presence(models.Model):
    id = models.AutoField(primary_key=True)
    course_session = models.ForeignKey(Course_session, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    entrance_time =  models.DateTimeField(auto_now_add=True)


    class Meta:  
        #so one student cannot register himself twice in same session
        unique_together = ('course_session', 'student',)

    def __str__(self):
        return str(self.student) 
