# Generated by Django 4.2.1 on 2023-05-29 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Departments', '0020_alter_courses_fee_structure'),
    ]

    operations = [
        migrations.AddField(
            model_name='about_us',
            name='History_image',
            field=models.ImageField(blank=True, null=True, upload_to='History_pics'),
        ),
        migrations.AddField(
            model_name='about_us',
            name='VisionAndValues_image',
            field=models.ImageField(blank=True, null=True, upload_to='VisionAndValues_pics'),
        ),
    ]
