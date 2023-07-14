from django.shortcuts import render,get_object_or_404
#from django.http import HttpResponse
# Create your views here.
from Departments.models import Departments,News,FAQ,Location_Info,About_Us,Students,Courses
from .forms import StudentProfileForm
from django.contrib.auth.decorators import login_required
from users.decorators import unauthenticated_user,allowed_users,admin_only


def Home(request):
    location = Location_Info.objects.all()
    faq = FAQ.objects.all()
    departments = Departments.objects.all()
    news = News.objects.all()
    context = {
        'departments': departments,
        'news': news,
        'faq': faq,
        'location': location,
    }
    return render(request, 'Departments/home.html', context)
def About(request):
    abt=About_Us.objects.all()

    location=Location_Info.objects.all()
    faq=FAQ.objects.all()
    departments=Departments.objects.all()
    news=News.objects.all()

    context={'abt':abt,
            'departments':departments,
            'news':news,
            'faq':faq,
            'location':location,
            }
    #return HttpResponse('hello world')
    return render(request,'Departments/about.html',context)
# def contact(request):
#     context={}
#     #return HttpResponse('hello world')
#     return render(request,'Departments/contact.html',context)
@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def userpage(request):
    student = request.user.students
    courses = student.course if student else None
    print('COURSES:', courses)

    location=Location_Info.objects.all()
    faq=FAQ.objects.all()
    departments=Departments.objects.all()
    news=News.objects.all()

    context = {'courses': courses,
            'departments':departments,
            'news':news,
            'faq':faq,
            'location':location,

                }
    return render(request, 'Departments/userpage.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def user_profile(request):
    student = request.user.students
    form = StudentProfileForm(instance=student)
    print('image:',student.profile_pic.url)

    location=Location_Info.objects.all()
    faq=FAQ.objects.all()
    departments=Departments.objects.all()
    news=News.objects.all()

    if request.method == 'POST':
        form = StudentProfileForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
    context = {
                'form': form,
                'departments':departments,
                'news':news,
                'faq':faq,
                'location':location,
                }
    return render(request, 'Departments/profile.html', context)



def news_detail(request, pk):

    news = get_object_or_404(News, pk=pk)

    context = {
        'news': news
    }
    return render(request, 'Departments/news_detail.html', context)
