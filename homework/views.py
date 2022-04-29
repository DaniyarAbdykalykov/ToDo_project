from django.shortcuts import render, HttpResponse
from .models import ToMeet

def homework(request):
    return render(request, 'homework.html')

def welcomepage(request):
    return HttpResponse('Добро пожаловать в приложение ToDo - Admin')

def meeting(request):
    tomeet_list = ToMeet.objects.all()
    return render(request, 'meeting.html', {'tomeet_list': tomeet_list})

