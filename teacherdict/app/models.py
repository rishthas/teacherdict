from django.db import models

# Create your models here.
class Subject(models.Model):
    subject_name    =   models.CharField(max_length=100,null=False)
    subject_desc    =   models.CharField(max_length=200)
    def __str__(self):
        return self.subject_name

class Teacher(models.Model):
    first_name  =   models.CharField(max_length=100)
    last_name   =   models.CharField(max_length=100)
    profil_pic  =   models.ImageField(upload_to ='pictures/',max_length=255,null=True,blank=True)
    email_id    =   models.EmailField(max_length=100,unique=True)
    phone_no    =   models.CharField(max_length=12)
    room_no     =   models.CharField(max_length=10)
    subjects    =   models.ManyToManyField(Subject,related_name='teachers')
    def __str__(self):
        return self.first_name


    
