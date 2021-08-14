from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def tasklist(resquest):
    return HttpResponse('To Do List')