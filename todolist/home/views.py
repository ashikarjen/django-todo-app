from django.shortcuts import render, HttpResponse, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import *
from .forms import CreateUserForm

# Create your views here.
def registration(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('/login')

    context = {'form':form}
    return render(request, 'reg.html', context)
     


def loginPage(request):
    
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            messages.info(request, 'Invalid Username Or Password')
            context = {}
            return render(request, 'login.html', context)
    
    context = {}

    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('/login')

@login_required(login_url='loginPage')
def home(request):
    context = {'success': False}
    if request.method=="POST":
        title = request.POST['title']
        desc = request.POST['desc']
        ins = Task(taskTitle=title, taskDesc=desc, taskUrl="#")
        ins.save()
        context = {'success': True}

    return render(request, 'index.html', context)

@login_required(login_url='loginPage')
def tasks(request):
    allTasks = Task.objects.all()
    context = {'tasks': allTasks}
    return render(request, 'tasks.html', context)
