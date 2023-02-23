from django.urls import path
from . import views

urlpatterns = [
path('',views.home,name='home'),
path('todo-list',views.todo,name='todo'),
path('create-todo',views.addtodo,name='addtodo'),
path('edit-todo<int:pk>',views.edit,name='edit'),
path('delete-todo<int:pk>',views.deletetodo,name='deletetodo')
]
