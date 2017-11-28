from django.conf.urls import url

from . import views

print "reached"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^todo/', views.todo, name='todo'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^Homeworkorganizer/', views.Homeworkorganizer, name='Homeworkorganizer'),
    url(r'^notepad/', views.notepad, name='notepad'),
    url(r'^studygroup/', views.studygroup, name="studygroup"),
    url(r'^todo/newtodo\S+', views.todo_new, name='new_todo_elem')
]
