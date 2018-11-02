from django.shortcuts import render
import datetime as dt

def welcome(request):
    return render(request, 'welcome.html')
