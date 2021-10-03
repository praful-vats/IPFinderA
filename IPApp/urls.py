from django.urls import path
# from django.conf.urls import patterns, url

from . import views


urlpatterns = [
    path('', views.index, name='index'),
]
# urlpatterns = patterns('IPApp.views', url(r'^list/$', 'list', name='list'),)
