from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^todo/', views.todo, name='todo'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^Homeworkorganizer/', views.Homeworkorganizer, name='Homeworkorganizer'),
    url(r'^notepad/', views.notepad, name='notepad'),
]
