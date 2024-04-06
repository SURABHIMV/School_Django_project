from django.contrib import admin
from .models import Teacher
from .models import Student
from django.utils.html import format_html

class TeacherAdmin(admin.ModelAdmin):    # https://medium.com/django-unleashed/django-admin-displaying-images-in-your-models-bb7e9d8be105
    def image_tag(self, obj):
        if obj.Image:  # Ensure there's an image associated with the object
            return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.Image.url))
        else:
            return 'No Image'

    image_tag.short_description = 'Teacher Image'
    list_display = ['Name', 'image_tag', 'Age', 'Email', 'Contact', 'Teaching_area']

class StudentAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        if obj.Image1:  # Ensure there's an image associated with the object
            return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.Image1.url))
        else:
            return 'No Image'

    image_tag.short_description = 'Student Image'
    list_display = ['Name', 'image_tag', 'Date_of_birth', 'Email', 'Class', 'Blood_group','Parent_Contact','Marks']
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student,StudentAdmin)