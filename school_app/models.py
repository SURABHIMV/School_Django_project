from django.db import models
class Teacher(models.Model):

   Name = models.CharField(max_length=100,null=True)
   Image=models.ImageField(upload_to="teacher_image_admin/", null=True, blank=True)
   Age=models.IntegerField(null=True, blank=True)
   Email=models.EmailField(null=True, blank=True)
   Contact=models.PositiveBigIntegerField(null=True)
   Teaching_area=models.CharField(max_length=100,null=True)

class Student(models.Model):
    Name = models.CharField(max_length=100,null=True)
    Image1=models.ImageField(upload_to="student_image_admin/", null=True, blank=True)
    Date_of_birth = models.DateField(null=True)
    Email=models.EmailField(null=True, blank=True)
    Class=models.CharField(max_length=100,null=True)
    Blood_group=models.CharField(max_length=10,null=True)
    Parent_Contact=models.PositiveBigIntegerField(null=True)
    Marks=models.CharField(max_length=10,null=True)
