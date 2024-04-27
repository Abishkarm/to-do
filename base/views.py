from importlib.resources import contents
from django.shortcuts import render
from django.http import HttpResponse
from .models import todo
# Create your views here.
def home(request):
    todos=todo.objects.all()
    content = {'todos':todos}
    return render(request,'index.html', context=content)

