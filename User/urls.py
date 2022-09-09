from django.urls import path

from . import views

urlpatterns = [
    path('register', views.registration, name='register'),
    path('log-in', views.login, name='log-in'),
    path('change_pass', views.change_password, name='change_pass')
]