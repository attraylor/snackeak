from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


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
    print("reachedtodo")
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

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import TodoForm, ClassChatForm

def todo_new(request):
    print("reached todonew")
    if request.method == "POST":
        form = TodoForm(request.POST)
        print("post", form.is_valid())
        if form.is_valid():
            print("post valid")
            todo_inst = form.save(commit=False)

            todo_inst.activity = form.cleaned_data["activity"]
            todo_inst.student = Student.objects.filter(email =request.user.email)[0]
            if request.user.is_authenticated():
                print("user authenticated!")
            todo_inst.save()
            return HttpResponseRedirect(reverse('todo'))
    else: #GET
        print("get")
        form = TodoForm()
    return render(request, 'todo.html', {'form': form})

from time import gmtime, strftime
def chat_new(request):
    print("reached chatnew")
    if request.method == "POST":
        form = ClassChatForm(request.POST)
        print("post", form.is_valid())
        if form.is_valid():
            print("post valid")
            class_inst = form.save(commit=False)
            class_to_update = Class.objects.filter(student__email=request.user.email)[0]
            student_name = Student.objects.filter(email=request.user.email)[0]
            class_to_update.chat += "{} {}:\t{}\n".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()), student_name.name, form.cleaned_data["chat"])
            class_to_update.save()
            if request.user.is_authenticated():
                print("user authenticated!")
            class_to_update.save()
            return HttpResponseRedirect(reverse('studygroup'))
    else: #GET
        print("get")
        form = ClassChatForm()
    return render(request, 'studygroup.html', {'form': form})

def note_new(request):
    print("reached note_new")
    if request.method == "POST":
        form = NoteForm(request.POST)
        print("post", form.is_valid())
        if form.is_valid():
            print("post valid")
            note_inst = form.save(commit=False)
            note_inst.note = form.cleaned_data["note"]
            note_inst.classes = form.cleaned_data["class"]
            note_inst.title = form.cleaned_data["class"]
            if request.user.is_authenticated():
                print("user authenticated!")
            todo_inst.save()
            return HttpResponseRedirect(reverse('todo'))
    else: #GET
        print("get")
        form = TodoForm()
    return render(request, 'todo.html', {'form': form})

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class TodoUpdate(UpdateView):
    model = Todo
    fields = ['activity']
    def get_success_url(self):
        return reverse('todo')

class TodoDelete(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo')
