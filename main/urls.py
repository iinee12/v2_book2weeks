from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index),
    path('book/', views.bookpage),
    path('bookDetail/', views.bookDetail),
    path('readinglist/', views.readinglist),
    path('readingwrite/', views.readingWirte),
    url(r'^summernote/', include('django_summernote.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
