# Generated by Django 4.2.1 on 2023-05-25 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Departments', '0012_students_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Departments.students'),
        ),
    ]