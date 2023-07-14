from Departments.models import Students,Courses,Departments
from django.forms import ModelForm

class StudentForm(ModelForm):
    class Meta:
        model=Students
        fields='__all__'
        exclude=['user']
class CourseForm(ModelForm):
    class Meta:
        model = Courses
        fields = '__all__'

class DepartmentForm(ModelForm):
    class Meta:
        model = Departments
        fields = '__all__'
