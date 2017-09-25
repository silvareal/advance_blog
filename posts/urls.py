from django.conf.urls import url
from django.contrib import admin

from . import views


app_name = 'posts'
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^create/$', views.post_create, name='post_create'),
    url(r'^(?P<slug>[\w-]+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<slug>[\w-]+)/edit$', views.post_update, name='post_update'),
    url(r'^(?P<slug>[\w-]+)/delete$', views.post_delete, name='post_delete'),
]


    