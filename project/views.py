from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from etl.etl_data import df_vun1
import json

#from .models import Task

def taskList(request):
    tasks = 'teste'
    return render(request, 'layout/list.html', {'tasks': tasks})

def helloWord(request):
    return HttpResponse('Teste')

def Table(request):
    json_records = df_vun1.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}
  
    return render(request, 'layout/table.html', context)