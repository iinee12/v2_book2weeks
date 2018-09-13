from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index),
    path('book/', views.bookpage),
    path('nowbook/', views.nowbookCall),
    path('nowbooksendelete/', views.nowbooksendelete),
    path('nowbookscoredelete/', views.nowbookscoredelete),
    path('nowbooksendeletefordetail/', views.nowbooksendeletefordetail),
    path('nowbookscoredeletefordetail/', views.nowbookscoredeletefordetail),
    path('nextbook/', views.nextbook),
    url(r'^wishBookdetail/$', views.post_wishBookdetail, name='post_wishBookdetail'),
    path('nextbooksearch/', views.nextbooksearch),
    path('scoreregistfordetail/', views.scoreregistfordetail),
    path('scoreregist/', views.scoreregist),
    path('bookDetail/', views.bookDetail),
    path('readinglist/', views.readinglist),
    path('readingChange/', views.readingChange),
    path('readingwrite/', views.readingWirte),
    path('readingdetail/', views.readingdetail),
    path('meetingmain/', views.meetingmain),
    path('meeting/', views.meetingdetail),
    url(r'^login/$', views.signin, name='/login'),
    url(
        r'^accounts/logout/',
        auth_views.logout,
        name='logout',
        kwargs={
            'next_page': settings.LOGIN_URL,
        }
    ),
    url(r'^summernote/', include('django_summernote.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
