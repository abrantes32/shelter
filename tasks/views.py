from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from etl.etl_data import df_vun 
import json

from .models import Task

def taskList(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/list.html', {'tasks': tasks})

def helloWord(request):
    return HttpResponse('Teste')

def yourName(request, name):
    return render(request, 'tasks/yourname.html', {'name': name})

def Table(request):  
    json_records = df_vun.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}
  
    return render(request, 'tasks/table.html', context)