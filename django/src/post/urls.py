from django.contrib import admin
from django.urls import path, re_path
from post import views

urlpatterns = [
    path('index/', views.index),
    re_path(r'^about/s/$', views.about), 
    re_path(r'^g+/$', views.ggg),
    re_path(r'^contact(?:s)?/$', views.contacts),
    re_path(r'^archive/\d{4}/$', views.archive),
    re_path(r'^archive_2/1[7-9]\d{2}/$', views.archive_2),
    re_path(r'^group/[a-cA-C]\d{4}/$', views.group),
    re_path(r'^home/', views.home_1),
]
