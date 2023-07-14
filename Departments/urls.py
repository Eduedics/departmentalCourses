
from django.urls import path
from Departments import views as department_views

urlpatterns = [
    path('',department_views.Home,name='home'),
    # path('about/',department_views.About,name='about'),
    path('userpage/',department_views.userpage,name='userpage'),
    path('profile/',department_views.user_profile,name='profile'),
    # path('contact/',department_views.contact,name='contact'),
    path('news/<int:pk>/', department_views.news_detail, name='news_detail'),
]
