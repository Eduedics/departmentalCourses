# Generated by Django 4.2.1 on 2023-05-28 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Departments', '0017_remove_courses_student_alter_courses_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='profile_pic',
            field=models.ImageField(blank=True, default='/Edu.jpg', null=True, upload_to='profile_pics'),
        ),
    ]