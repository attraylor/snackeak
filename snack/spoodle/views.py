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

def notepad(request):
    """
    View function for home page of site.
    """
    notepad = Notepad.objects.all()



    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'notepad.html',
        context={'notepad':notepad},
    )

def contact(request):
    """
    View function for home page of site.
    """
    contact = Contact.objects.all()



    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'contact.html',
        context={'contact':contact},
    )

def Homeworkorganizer(request):
    """
    View function for home page of site.
    """
    homeworkorganizer = Homework.objects.all()



    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'Homeworkorganizer.html',
        context={'homeworkorganizer':homeworkorganizer},
    )


def studygroup(request):
    """
    View function for home page of site.
    """
    students = Student.objects.all()



    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'studygroup.html',
        context={'students':students},
    )
