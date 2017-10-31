from django.shortcuts import render

# Create your views here.
from .models import Class, Student, Todo, Professor, Homework, Note

def index(request):
    """
    View function for home page of site.
    """
    classes = Class.objects.all()



    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'classes':classes},
    )


def todo(request):
    """
    View function for home page of site.
    """
    todos = Todo.objects.all()



    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'todo.html',
        context={'todos':todos},
    )
