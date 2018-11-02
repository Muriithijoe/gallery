from django.http  import HttpResponse,Http404
import datetime as dt
from django.shortcuts import render,redirect
from .models import Photo

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')
