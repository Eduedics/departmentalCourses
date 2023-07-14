from .models import Students,Courses
from django.forms import ModelForm

class StudentProfileForm(ModelForm):
    class Meta:
        model = Students
        fields = '__all__'
        exclude = ['user']

