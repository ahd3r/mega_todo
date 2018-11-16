"""mega_todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo_list import views

urlpatterns = [
    path('a/', admin.site.urls),
    path('', views.home, name='home'),
    path('my_logout', views.my_logout, name='my_logout'),
    path('delete_all', views.delete_all, name='delete_all'),
    path('delete_completed', views.delete_completed, name='delete_completed'),
    path('add_task', views.add_task, name='add_task'),
    path('completed/<task_id>', views.completed, name='completed'),
    path('delete_one/<t_id_delete>', views.delete_one, name='delete_one'),
    path('edit_one/<t_id_edit>', views.edit_one, name='edit_one'),
]
