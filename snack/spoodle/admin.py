from django.contrib import admin

# Register your models here.
from .models import Class, Student, Todo, Professor, Homework, Note
admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Todo)
admin.site.register(Professor)
admin.site.register(Homework)
admin.site.register(Note)