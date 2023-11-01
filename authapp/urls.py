from django.contrib import admin
from django.urls import path
from authapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('inner/', views.inner, name='inner'),
    path('doctors/', views.doctors, name='doctors'),
    path('department/', views.department, name='department'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('about/', views.about, name='about'),
    path('appointment/', views.appointment, name='appointment'),
]