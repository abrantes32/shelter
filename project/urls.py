from django.urls import path

from . import views

urlpatterns = [
    path('', views.taskList, name='task-list'),
    path('tables', views.Table, name ="table"),

]