# Generated by Django 4.2.1 on 2023-05-29 08:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='IQTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('choice1', models.CharField(max_length=255)),
                ('choice2', models.CharField(max_length=255)),
                ('choice3', models.CharField(max_length=255)),
                ('choice4', models.CharField(max_length=255)),
                ('correct_answer', models.CharField(max_length=255)),
                ('score', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]