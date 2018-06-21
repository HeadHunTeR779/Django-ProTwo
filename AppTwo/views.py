from django.shortcuts import render
from django.http import HttpResponse
import os
from .models import User

# Create your views here.

def index(request):
    return HttpResponse('<h4>In Above url just append /user</h4>')

def help(request):
    user_list = User.objects.order_by('last_name')  #you may also do User.objects.all('last_name')
    context_dict = {'user_details':user_list}
    path = os.path.join(os.getcwd(), "templates", "AppTwo", "user.html")
    return render(request, path, context_dict)
