# Generated by Django 5.0.3 on 2024-04-03 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0008_alter_student_image1'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Marks',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Image1',
            field=models.ImageField(blank=True, null=True, upload_to='student_image_admin/'),
        ),
    ]
