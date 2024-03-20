from django.db import models
class Teacher(models.Model):

   Name = models.CharField(max_length=100)
   Image = models.ImageField(upload_to='pics')
   Date_of_birth = models.DateField()
   Age=models.IntegerField(null=True, blank=True, verbose_name='Age of the person')
   Email=models.EmailField(null=True, blank=True, verbose_name='Email address')
   Contact=models.PositiveBigIntegerField()
   Teaching_area=models.CharField(max_length=100)
   Address=models.CharField(max_length=200,null=True)

class Student(models.Model):
    Name = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='pics')
    Date_of_birth = models.DateField()
    Age=models.IntegerField(null=True, blank=True, verbose_name='Age of the person')
    Email=models.EmailField(null=True, blank=True, verbose_name='Email address')
    Class=models.CharField(max_length=100)
    Blood_group=models.CharField(max_length=20)
    Parent_Contact=models.PositiveBigIntegerField()
    Address=models.CharField(max_length=200,null=True)