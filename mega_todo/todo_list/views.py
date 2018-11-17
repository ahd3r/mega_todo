from django.shortcuts import render, redirect
from .models import TodoListModel
from django.contrib.auth import logout, authenticate, login
from .forms import AddToDoForm, LogInForm, SignUpForm, EditOneForm, ResetPasswordForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
# from django.contrib.auth.hashers import make_password
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
@login_required
def add_task(request):
    TodoListModel(name=request.POST['name'], user=request.user).save()
    return redirect('home')

@login_required
def delete_completed(request):
    todolist=TodoListModel.objects.filter(user=request.user)
    for todo in todolist:
        if todo.done==True:
            todo.delete()
    return redirect('home')

@login_required
def delete_all(request):
    todolist=TodoListModel.objects.filter(user=request.user)
    todolist.delete()
    return redirect('home')

@login_required
def completed(request, task_id):
    try:
        todolist=TodoListModel.objects.get(id=task_id, user=request.user)
    except TodoListModel.DoesNotExist:
        return render(request, '404.html')
    else:
        if todolist.done==True:
            todolist.done=False
        else:
            todolist.done=True
        todolist.save()
        return redirect('home')

@login_required
def delete_one(request, t_id_delete):
    try:
        TodoListModel.objects.get(id=t_id_delete, user=request.user)
    except TodoListModel.DoesNotExist:
        return render(request, '404.html')
    else:
        TodoListModel.objects.get(id=t_id_delete).delete()
        return redirect('home')

@login_required
def edit_one(request, t_id_edit):
    if request.POST:
        task=TodoListModel.objects.get(id=t_id_edit)
        task.name=request.POST['name_task']
        if request.POST.get('done_task', False)=='on':
            task.done=True
        if request.POST.get('done_task', False)==False:
            task.done=False
        task.save()
        return redirect('home')
    try:
        TodoListModel.objects.get(user=request.user, id=t_id_edit)
    except TodoListModel.DoesNotExist:
        return render(request, '404.html')
    else:
        context={
            'EditOneForm':EditOneForm,
            't_id_edit':t_id_edit,
        }
        return render(request, 'edit_one.html', context)

@login_required
def setting(request):
    if request.POST:
        user_for_reset=request.user
        if user_for_reset.check_password(request.POST['old_password'])==True and request.POST['new_password1']==request.POST['new_password2']:
            user_for_reset.set_password(request.POST['new_password2'])
            user_for_reset.save()
            user_in=authenticate(request, username=request.user.username, password=request.POST['new_password2'])
            login(request, user_in)
            return redirect('home')
        else:
            return render(request, '404.html')
    context={
        'ResetPasswordForm':ResetPasswordForm,
    }
    return render(request, 'setting.html', context)

@login_required
def delete_account(request):
        account=request.user
        account.is_active=False
        account.save()
        # logout(request)
        return redirect('home')
