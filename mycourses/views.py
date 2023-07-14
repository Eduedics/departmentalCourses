from django.shortcuts import render
from Departments.models import Departments,News,FAQ,Location_Info,About_Us,Students,Courses
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from users.decorators import unauthenticated_user,allowed_users,admin_only


# Create your views here.
@login_required(login_url='login')
def courses(request):
    all_courses = Courses.objects.all()
    paginator = Paginator(all_courses, 10)  # Display 10 courses per page
    page_number = request.GET.get('page')  # Get the current page number from the request
    page_obj = paginator.get_page(page_number)  # Get the Page object for the current page

    location=Location_Info.objects.all()
    faq=FAQ.objects.all()
    departments=Departments.objects.all()
    news=News.objects.all()

    context = {
        'page_obj': page_obj,
        'departments':departments,
        'news':news,
        'faq':faq,
        'location':location,
    }
    return render(request, 'mycourses/courses.html', context)

@login_required(login_url='login')
def departmentcourses(request,department_id):
    department = Departments.objects.get(id=department_id)
    courses = Courses.objects.filter(department=department)

    location=Location_Info.objects.all()
    faq=FAQ.objects.all()
    departments=Departments.objects.all()
    news=News.objects.all()

    return render(request, 'mycourses/departmentcourses.html',
        {'courses': courses,
        'departments':departments,
        'news':news,
        'faq':faq,
        'location':location,}
        )

# def course_detail(request, course_id):
#     course = get_object_or_404(Courses, id=course_id)
#     context = {
#         'course': course,

#     }
#     return JsonResponse({
#         'overview': course.overview,
#         'course_structure': course.course_structure,
#         'admission_requirement': course.admission_requirement,
#         'fee_structure': course.fee_structure.url if course.fee_structure else '',
#     })
#     return render(request,'mycourses/courses.html',context)
@login_required(login_url='login')
def course_detail(request, course_id):
    course = get_object_or_404(Courses, id=course_id)
    overview = course.overview

    location=Location_Info.objects.all()
    faq=FAQ.objects.all()
    departments=Departments.objects.all()
    news=News.objects.all()

    context = {
        'course': course,
        'overview': overview,
        'departments':departments,
        'news':news,
        'faq':faq,
        'location':location,

    }
    return render(request, 'mycourses/courses_detail.html', context)

@login_required(login_url='login')
def search_courses(request):
    query = request.GET.get('query')  # Get the search query from the request
    courses = Courses.objects.filter(name__icontains=query) if query else []

    location=Location_Info.objects.all()
    faq=FAQ.objects.all()
    departments=Departments.objects.all()
    news=News.objects.all()

    context = {
        'query': query,
        'courses': courses,
        'departments':departments,
        'news':news,
        'faq':faq,
        'location':location,
    }
    return render(request, 'mycourses/search_courses.html', context)
