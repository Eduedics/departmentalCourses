"""
URL configuration for Courses project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from mycourses import views as Courses_views
from users import views as user_views
from Staff_panel import views as Staff_panel_views
from Iq_Test import views as Iqtest_views
from django.contrib.auth import views as auth_views
from contactus import views as contactus_views
from About import views as About_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Departments.urls')),

    path('about/',About_views.about_view,name='about'),
    path('history/',About_views.history_view,name='history'),

    path('courses/',Courses_views.courses,name='courses'),
    path('courses_detail/<int:course_id>/', Courses_views.course_detail, name='course_detail'),
    path('departmentcourses/<int:department_id>/',Courses_views.departmentcourses,name='departmentcourses'),
    path('search-courses/', Courses_views.search_courses, name='search_courses'),

    path('courses_detail/<int:course_id>/overview/', Courses_views.course_detail, name='course_overview'),

    path('feedback/', contactus_views.feedback, name='feedback'),
    path('success/', contactus_views.success, name='success'),

    path('register/',user_views.Register,name='register'),
    path('login/',user_views.login_user,name='login'),
    path('logout/',user_views.logout_user,name='logout'),
    path('success_enrollment/',user_views.success_enrollment,name='success_enrollment'),

    # path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    # path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),

    path('attach_certificate/',user_views.attach_certificate,name='attach_certificate'),

    path('dashboard/',Staff_panel_views.Admin_home,name='dashboard'),
    path('student/<str:pk>/',Staff_panel_views.student,name='student'),

    path('students/create/', Staff_panel_views.create_student, name='create_student'),
    path('students/<int:pk>/update/', Staff_panel_views.update_student, name='update_student'),
    path('students/<int:pk>/delete/', Staff_panel_views.delete_student, name='delete_student'),

    path('courses/create/', Staff_panel_views.create_course, name='create_course'),
    path('courses/<int:pk>/update/', Staff_panel_views.update_course, name='update_course'),
    path('courses/<int:pk>/delete/', Staff_panel_views.delete_course, name='delete_course'),

    path('department/create/', Staff_panel_views.create_department, name='create_department'),
    path('department/<int:pk>/update/', Staff_panel_views.update_department, name='update_department'),
    path('department/<int:pk>/delete/', Staff_panel_views.delete_department, name='delete_department'),


    path('iqtest/', Iqtest_views.iq_test, name='iq_test'),
    path('score/', Iqtest_views.iq_test_results, name='score'),

    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='Departments/password_reset.html'),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='Departments/password_reset_sent.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='Departments/password_reset_form.html'),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='Departments/password_reset_done.html'),name='password_reset_complete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_URL)
