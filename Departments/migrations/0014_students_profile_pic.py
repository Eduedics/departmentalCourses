# Generated by Django 4.2.1 on 2023-05-25 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Departments', '0013_courses_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
