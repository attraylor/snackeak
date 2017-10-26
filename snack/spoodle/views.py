from django.shortcuts import render

# Create your views here.
from .models import Class, Student, Todo, Professor, Homework, Note

def index(request):
    """
    View function for home page of site.
    """
    classses = Class.objects.all()


    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'classes':classes},
    )
