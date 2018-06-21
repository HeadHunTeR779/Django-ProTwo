from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.

def index(request):
    return HttpResponse('<em>MySecondApp</em>')

def help(request):
    context_dict = {'text_here' : "Help Page Trolol"}
    path = os.path.join(os.getcwd(), "templates", "AppTwo", "help.html")
    return render(request, path, context_dict)
