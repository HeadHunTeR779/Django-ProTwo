from django.shortcuts import render
from django.http import HttpResponse
from .forms import MyModelForm

# Create your views here.

def index(request):
    return render(request, 'AppTwo/index.html')

def user(request):
    form = MyModelForm()

    if request.method == "POST":
        form = MyModelForm(request.POST)

        form.save()



    return render(request, 'AppTwo/user.html', context={'form':form})
