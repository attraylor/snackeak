from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^todo/$', views.todo, name='todo'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^Homeworkorganizer/', views.Homeworkorganizer, name='Homeworkorganizer'),
    url(r'^notepad/$', views.notepad, name='notepad'),
    url(r'^studygroup/$', views.studygroup, name="studygroup"),
    url(r'^todo/newtodo/', views.todo_new, name='new_todo_elem'),
    url(r'^studygroup/newchat/', views.chat_new, name='new_chat_elem'),
    url(r'^notepad/newnote/', views.note_new, name='new_note_elem'),

]
