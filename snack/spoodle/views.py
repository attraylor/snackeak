from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Class, Student, Todo, Professor, Homework, Note

@login_required
def index(request):
    """
    View function for home page of site.
    """
    classes = Class.objects.filter(student__email=request.user.email)



    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'classes':classes},
    )

@login_required
def todo(request):
    """
    View function for home page of site.
    """
    print "reachedtodo"
    todos = Todo.objects.filter(student__email = request.user.email)



    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'todo.html',
        context={'todos':todos},
    )

@login_required
def notepad(request):
    """
    View function for home page of site.
    """
    classlist = Class.objects.filter(student__email=request.user.email)
    notepad = Note.objects.filter(classes__in=classlist)



    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'notepad.html',
        context={'notepad':notepad, 'classlist':classlist},
    )

@login_required
def contact(request):
    """
    View function for home page of site.
    """
    classlist = Class.objects.filter(student__email=request.user.email)
    contact = Professor.objects.filter(classes__in=classlist)



    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'contact.html',
        context={'contact':contact},
    )

@login_required
def Homeworkorganizer(request):
    """
    View function for home page of site.
    """
    classlist = Class.objects.filter(student__email=request.user.email)
    homeworkorganizer = Homework.objects.filter(classes__in=classlist)



    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'Homeworkorganizer.html',
        context={'homeworkorganizer':homeworkorganizer, 'classlist':classlist},
    )

@login_required
def studygroup(request):
    """
    View function for home page of site.
    """
    classlist = Class.objects.filter(student__email=request.user.email)



    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'studygroup.html',
        context={'classlist':classlist},
    )

def todo_new(request):
    print "reached todonew"
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'todo.html', {'form': form})
        else: #GET
            return render(request, 'todo.html', {'form': form})
