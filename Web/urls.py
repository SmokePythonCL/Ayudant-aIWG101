from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_view),
    path('ayudantia/', views.ayudantia_view),
]