from django.shortcuts import render, redirect
from .models import TodoListModel
from django.contrib.auth import logout, authenticate, login
from .forms import AddToDoForm, LogInForm, SignUpForm, EditOneForm
from django.views.decorators.http import require_POST
# from django.views import generic

def home(request):
    if request.user.is_authenticated:
        todolist=TodoListModel.objects.filter(user=request.user)
        context={
            'AddToDoForm': AddToDoForm,
            'todolist': todolist,
        }
        return render(request, 'home_user.html',context)
    else:
        context={
            'LogInForm':LogInForm,
            'SignUpForm':SignUpForm,
        }
        return render(request, 'home_enter.html', context)

def my_logout(request):
    logout(request)
    return redirect(home)

@require_POST
def add_task(request):
    TodoListModel(name=request.POST['name'], user=request.user).save()
    return redirect('home')

def delete_completed(request):
    todolist=TodoListModel.objects.filter(user=request.user)
    for todo in todolist:
        if todo.done==True:
            todo.delete()
    return redirect('home')

def delete_all(request):
    todolist=TodoListModel.objects.filter(user=request.user)
    todolist.delete()
    return redirect('home')

def completed(request, task_id):
    todolist=TodoListModel.objects.get(id=task_id)
    if todolist.done==True:
        todolist.done=False
    else:
        todolist.done=True
    todolist.save()
    return redirect('home')

def delete_one(request, t_id_delete):
    TodoListModel.objects.get(id=t_id).delete()
    return redirect('home')

def edit_one(request, t_id_edit):
    if request.POST:
        task=TodoListModel.objects.get(id=t_id_edit)
        task.name=request.POST['name_task']
        task.done=request.POST['done_task']
        task.save()
        return redirect('home')
    context={
        'EditOneForm':EditOneForm,
        't_id_edit':t_id_edit,
    }
    return render(request, 'edit_one.html', context)
