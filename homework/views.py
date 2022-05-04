from django.shortcuts import render, HttpResponse, redirect
from .models import ToMeet, Goal_for_month

def homework(request):
    return render(request, 'homework.html')

def welcomepage(request):
    return HttpResponse('Добро пожаловать в приложение ToDo - Admin')

def meeting(request):
    tomeet_list = ToMeet.objects.all()
    return render(request, 'meeting.html', {'tomeet_list': tomeet_list})

def goal_for_month(request):
    goal_for_month_list = Goal_for_month.objects.all()
    return render(request, 'goal_for_month.html', {'goal_for_month_list': goal_for_month_list})

def add_meeting(request):
    form = request.POST
    persone = form['todo_persone']
    phone_number = form['meeting_phone']
    date_of_meeting = form['meeting_date']
    comment = form['meeting_comment']
    tomeet = ToMeet(persone=persone, phone_number=phone_number, comment=comment, date_of_meeting=date_of_meeting)
    tomeet.save()
    return redirect(meeting)

