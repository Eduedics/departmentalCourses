from django.shortcuts import render,redirect
from Departments.models import Departments,Courses,Students
from .forms import StudentForm,CourseForm,DepartmentForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from users.decorators import unauthenticated_user,allowed_users,admin_only


# Create your views here.
# def Admin_home(request):
#     departments=Departments.objects.all()
#     course=Courses.objects.all()
#     student=Students.objects.all()

#     total_departments=departments.count()
#     total_course=course.count()
#     total_student=student.count()
#     context={
#             'departments':departments,
#             'course':course,
#             'student':student,
#             'total_departments':total_departments,
#             'total_student':total_student,
#             'total_course':total_course,
#             }
#     return render(request,'Staff_panel/dashboard.html',context)
@login_required(login_url='login')
@admin_only
def Admin_home(request):
    departments = Departments.objects.all()
    course = Courses.objects.all()
    student = Students.objects.all()

    total_departments = departments.count()
    total_course = course.count()
    total_student = student.count()

    # Pagination
    departments_paginator = Paginator(departments, 5)
    departments_page_number = request.GET.get('dept_page')
    departments_page_obj = departments_paginator.get_page(departments_page_number)

    course_paginator = Paginator(course, 5)
    course_page_number = request.GET.get('course_page')
    course_page_obj = course_paginator.get_page(course_page_number)

    student_paginator = Paginator(student, 5)
    student_page_number = request.GET.get('student_page')
    student_page_obj = student_paginator.get_page(student_page_number)

    context = {
        'departments': departments_page_obj,
        'course': course_page_obj,
        'student': student_page_obj,
        'total_departments': total_departments,
        'total_student': total_student,
        'total_course': total_course,
    }
    return render(request, 'Staff_panel/dashboard.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def student(request,pk):
    students=Students.objects.get(id=pk)
    # courses=Courses.students_set.all()
    total_courses = 1 if students.course else 0

    courses=Courses.objects.all()
    # total_courses = courses.students.all().count()
    # myfilter=CustomerOrderFilter(request.GET,queryset=orders)
    # orders=myfilter.qs
    student_count=courses.count()
    course=Courses.objects.all().count()
    context={'students':students,
            'courses':courses,
            'course':course,
            'student_count':student_count,
            'total_courses':total_courses,

            }
    return render(request,'Staff_panel/student.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def create_student(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save()
            return redirect('student', pk=student.pk)

    context = {'form': form}
    return render(request, 'Staff_panel/create_student.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def update_student(request, pk):
    student = Students.objects.get(pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student', pk=pk)
    else:
        form = StudentForm(instance=student)
    context = {'form': form}
    return render(request, 'Staff_panel/update_student.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def delete_student(request, pk):
    student = Students.objects.get(pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('dashboard')
    context = {'student': student}
    return render(request, 'Staff_panel/delete_student.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save()
            return redirect('dashboard')
    else:
        form = CourseForm()
    context = {'form': form}
    return render(request, 'Staff_panel/create_course.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def update_course(request, pk):
    course = Courses.objects.get(pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('student', pk=pk)
    else:
        form = CourseForm(instance=course)
    context = {'form': form}
    return render(request, 'Staff_panel/update_course.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def delete_course(request, pk):
    course = Courses.objects.get(pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('dashboard')
    context = {'course': course}
    return render(request, 'Staff_panel/delete_course.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def create_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save()
            return redirect('dashboard')
    else:
        form = DepartmentForm()
    context = {'form': form}
    return render(request, 'Staff_panel/create_department.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def update_department(request, pk):
    department = Departments.objects.get(pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, request.FILES, instance=department)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = DepartmentForm(instance=department)
    context = {'form': form}
    return render(request, 'Staff_panel/update_department.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def delete_department(request, pk):
    department = Departments.objects.get(pk=pk)
    if request.method == 'POST':
        department.delete()
        return redirect('dashboard')
    context = {'department': department}
    return render(request, 'Staff_panel/delete_department.html', context)
