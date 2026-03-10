from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('doctors/', views.doctors_view, name='doctors'),
    path('appointment/<str:doctor>/<str:spec>/', views.appointment_view, name='appointment'),
    path("logout/", views.logout_view, name="logout"),

]


