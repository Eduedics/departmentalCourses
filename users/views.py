from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import userregisterform,StudentsForm
from django.contrib.auth import login,authenticate,logout
from .decorators import unauthenticated_user,allowed_users
from django.contrib.auth.models import Group
from Departments.models import Students
from django.contrib.auth.decorators import login_required
from Departments.models import Departments,News,FAQ,Location_Info,About_Us,Students,Courses

# from users.decorators import unauthenticated_user,allowed_users,admin_only

# Create your views here.
@unauthenticated_user
def Register(request):
    form=userregisterform()
    if request.method=='POST':
        form=userregisterform(request.POST)
        if form.is_valid():
            user=form.save()
            # group=Group.objects.get(name='')
            # instance.group.add(group)
            # Students.objects.create(
            # user=instance,
            # name=instance.username,
            # )
            username=form.cleaned_data.get('username')
            messages.success(request,'Account created for '+ username)
            return redirect('login')

    context={'form':form}
    return render(request,'users/register.html',context)

@unauthenticated_user
def login_user(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')

    return render(request,'users/login.html')
def logout_user(request):
    logout(request)
    return redirect('login')
    return render(request,'users/logout.html')

@login_required(login_url='login')
def attach_certificate(request):

    location=Location_Info.objects.all()
    faq=FAQ.objects.all()
    departments=Departments.objects.all()
    news=News.objects.all()

    if request.method == 'POST':
        students_form = StudentsForm(request.POST, request.FILES)
        if students_form.is_valid():
            students_form.save()
            return redirect('success_enrollment')
    else:
        students_form = StudentsForm()

    context = {
        'students_form': students_form,
        'departments':departments,
        'news':news,
        'faq':faq,
        'location':location,
    }

    return render(request, 'users/attach_certificate.html', context)

def success_enrollment(request):

    return render(request, 'users/success_enrollment.html')
