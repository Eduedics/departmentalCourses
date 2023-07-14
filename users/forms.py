from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from Departments.models import Students

class userregisterform(UserCreationForm):
    email=forms.EmailField()
    # service_no=forms.CharField()

    class Meta:
        model=User
        fields=['username','email','password1','password2']


#file handling
# from django import forms
# class CertificateForm(forms.Form):
#     certificate = forms.FileField(label='Attach Certificate', help_text='Allowed file types: .pdf, .doc, .docx')

class StudentsForm(forms.ModelForm):
    certificate = forms.FileField(label='Attach Certificate', help_text='Allowed file types: .pdf, .doc, .docx')

    class Meta:
        model = Students
        fields = ['first_name', 'second_name', 'surname', 'service_no', 'id_no', 'course', 'qualifications', 'address', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['qualifications'].widget.attrs['multiple'] = True
        self.fields['qualifications'].widget.attrs['accept'] = 'application/pdf, application/msword, application/vnd.openxmlformats-officedocument.wordprocessingml.document'

    def save(self, commit=True):
        student = super().save(commit=False)
        student.certificate = self.cleaned_data.get('certificate')  # Access certificate file directly from cleaned data
        if commit:
            student.save()
        return student
