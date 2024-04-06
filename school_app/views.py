from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import admin
from .models import Student, Teacher
import os
from django.contrib.auth import authenticate,login
from django.contrib.auth.hashers import make_password, check_password
from django.conf import settings
from django.conf.urls.static import static
# Create your views here.
# Register your models here.
def HomePage(request):
    pass
signup_data = {}
def signupPage_teacher(request):
    if request.method=='POST':
        username=request.POST.get('username')
        try:
            image=request.FILES.get('image')
        except:
            image=""
        email=request.POST.get('email')
        age=request.POST.get('age')
        contact=request.POST.get('contact')
        Teaching_area=request.POST.get('teaching_area')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1!=password2:
            return HttpResponse("Password and confirm password are not same")
        else: 
          signup_data[username] = password1
          print(signup_data)
          print('teacher',username,email,password1,password2,image)
          my_teacher=Teacher.objects.create(Name=username,Image=image,Email=email,Age=age,Contact=contact,Teaching_area=Teaching_area)
          my_teacher.save()
          return redirect('login_teacher')
          #return HttpResponse("teacher data as been entered succesfully")
    return render(request,'signup_teacher.html')

def loginPage_teacher(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password1=request.POST.get('password')
        stored_password = signup_data.get(username)
        print(username, password1)
        print('stored_password',stored_password)
        if stored_password == password1:
            return redirect('admin_dashboard')
        else:
            return HttpResponse("Username Or Password is incorrect")

    return render(request,'login_teacher.html')

login_data = {}
stud_nam={}
def signupPage_student(request):
    if request.method=='POST':
        username=request.POST.get('username')
        try:
            image1=request.FILES.get('image1')
        except:
            image1=""
        email=request.POST.get('email')
        DoB=request.POST.get('date_of_Birth')
        p_contact=request.POST.get('parent_Contact')
        Blood_group=request.POST.get('blood_group')
        clas=request.POST.get('class')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1!=password2:
            return HttpResponse("Password and confirm password are not same")
        else: 
            login_data[username]=password1
            print('student',username,email,password1,password2,image1)
            my_student=Student.objects.create(Name=username,Image1=image1,Email=email,Date_of_birth=DoB,Parent_Contact=p_contact,Class=clas,Blood_group=Blood_group)
            my_student.save()
            return redirect('login_student')
    return render(request,'signup_student.html')

def loginPage_student(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('pass')
        stud_nam[0]=username
        stored_password = login_data.get(username)

        print(username, password)
        print('stored_password',stored_password)
        if stored_password == password:
            return redirect('student_profile_dashboard')

        else:
            return HttpResponse("Username or password are incorrect")
    return render(request,'login_student.html')


# dashboard/views.py
from django.shortcuts import render
from .models import Teacher, Student

# def admin_dashboard(request):
#     teachers = Teacher.objects.all()
#     students = Student.objects.all()
#     context = {
#         'teachers': teachers,
#         'students': students,
#     }
#     return render(request, 'dashboard.html', context)

def admin_dashboard(request):
    teachers = Teacher.objects.all()
    students = Student.objects.all()
    context = {
        'teachers': teachers,
        'students': students,
    }
    if request.method == 'POST':
        for student in Student.objects.all():
            print('######',student.Name)
            marks = request.POST.get(f'marks_{student.Name}')  # Use the student's primary key as part of the input name
            student.Marks = marks
            print('marks',marks)
            student.save()
    return render(request, 'dashboard.html', context)

def student_profile_dashboard(request):
    nam=stud_nam[0]
    print('nameeeeeeeeeeeeee',nam)
    for student in Student.objects.all():
        if student.Name==nam:
            student = Student.objects.get(Name=nam)
            context = {'stud': student}
            return render(request, 'demo.html', context) 

