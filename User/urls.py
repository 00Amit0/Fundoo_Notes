from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.Registration.as_view(), name='register'),
    path('log-in/', views.Login.as_view(), name='log-in'),
]
