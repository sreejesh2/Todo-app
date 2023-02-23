from django.shortcuts import render, redirect
from .models import *
from .forms import Todoform
from django.contrib import messages
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Todo

# Create your views here.


def home(request):
    return render(request, 'todoapp/home.html')


@login_required
def todo(request):
    try:
        form = Todo.objects.all().filter(user=request.user)
        context = {'form': form}
        return render(request, 'todoapp/todo.html', context)
    except:
        pass


@login_required
def addtodo(request):
    try:
        form = Todoform()

        if request.method == 'POST':
            form = Todoform(request.POST)
            if form.is_valid():
                todo = form.save(commit=False)
                todo.user = request.user
                todo.save()
                messages.success(request, "Todo Added successfully")
                return redirect('todo')

        context = {'form': form}
        return render(request, 'todoapp/add.html', context)
    except:
        pass


@login_required
def edit(request, pk):
    try:

        Todo_id = Todo.objects.get(id=pk)
        form = Todoform(instance=Todo_id)
        if request.method == "POST":
            form = Todoform(request.POST, instance=Todo_id)
            if form.is_valid():
                form.save()
                messages.success(request, "Updated successfully")
                return redirect('todo')

        context = {'form': form}
        return render(request, 'todoapp/update.html', context)
    except:
        pass


@login_required
def deletetodo(request, pk):
    try:
        form = Todo.objects.get(id=pk)
        form.delete()
        messages.info(request, "Deleted Successfully")
        return redirect('todo')
    except:
        pass
