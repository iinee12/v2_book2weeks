from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('book/', views.bookpage),
    path('bookDetail/', views.bookDetail),
]
