from importlib.resources import contents
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import todo
from django.urls import reverse
# Create your views here.
def home(request):
    todos=todo.objects.all()
    content = {'todos':todos}
    return render(request,'index.html', context=content)

def create(request):
    if request.method=="POST":
        name=request.POST.get("name")
        description=request.POST.get("description")
        status=request.POST.get("status")
        todo.objects.create(name=name,description=description,status=status)
        return redirect("home")
    return render(request,"create.html")

def edit(request, pk ):
    todo_obj=todo.objects.get(id=pk)
    if request.method=="POST":
        todo_obj.name=request.POST.get("name")
        todo_obj.description=request.POST.get("description")
        todo_obj.status=request.POST.get("status")
        todo_obj.save() 
        return redirect("home")
    content={'todo':todo_obj}
    return render(request,"edit.html",context=content)

# def delete(request,pk):
    # Replace with your actual model

def delete(request,pk):
    todo_obj=todo.objects.get(id=pk)

    # if request.method == 'POST':
        # Perform the file deletion operation here
        # For example, let's say you have a model 'YourModel' with a 'file' field
        # todo = request.POST.get('todo')  # You'll need to pass this from your template
    todo_objs = todo.objects.get()
    todo_objs.delete()
        
    # content={'todo':todo_obj}
    # return render(request,"delete.html",context=content)

# todo_obj=todo.objects.get(id=pk)
    return redirect("home")