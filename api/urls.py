
# from django.contrib import admin
from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
from .views import ping, post_list,post_detail

urlpatterns = [
    path('ping/', ping, name='ping'),
    path('posts/', post_list, name="post_list"),
    path('posts/<slug:slug>/', post_detail,name="post_detail"),
]


