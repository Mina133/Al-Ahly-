from django.urls import path
from . import views

urlpatterns = [
    path('', views.member_list, name='member_list'),
    path('create/', views.member_create, name='member_create'),
]