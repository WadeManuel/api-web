from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Task
from .forms import TasksForm
from django.contrib.auth.models import User
#Este login Es para las cookeis
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required


#Funcionalidad listar el index o base de nuestra web
def base(request):
    return render(request,'base.html')


#Vista tareas para las usuarios
@login_required
def tasks_list_pending(request):
    #datecomplet__isnull= True es que si ya fueron completadas que no salgan
    #es decir si tienen una fecha es por que ya fueron completadas si no tienn 
    #fecha es por que aun no aun sido completadas
    tasks = Task.objects.filter(user=request.user,datecompleted__isnull=True)
    return render(request,'tasks/listar.html',{'tasks':tasks})

@login_required
def tasks_completed(request):
    tasks = Task.objects.filter(user=request.user,datecompleted__isnull=False).order_by
    ('-datecompleted')
    return render(request,'tasks/listar.html',{'tasks':tasks})

#Funcionalidad para crear Tareas
@login_required
def create_task(request):
    if request.method=="GET":
        return render(request,'tasks/crear.html',{'form':TasksForm})
    else:
        try:
            form = TasksForm(request.POST)
            # Commit False es para solo me guarde
            # infor que esta dentro de cada campo de entrada
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            messages.add_message(request=request,level=messages.SUCCESS,message="Creat task success")
            return redirect('tasks')
        except ValueError:
            return render(request,'tasks/crear.html',{
                'form':form,
                'error':'Please provide valide data'
            })

@login_required
def task_detail(request,task_id):
    if request.method=="GET":   
        task=get_object_or_404(Task,pk=task_id,user=request.user)
        form=TasksForm(instance=task)
        return render(request,'tasks/editar.html',
        {   
            'task':task,
            'form':form
        })
    else:
        try :
            task=get_object_or_404(Task,pk=task_id,user=request.user)
            form=TasksForm(request.POST,instance=task)
            form.save()
            messages.add_message(request=request,level=messages.SUCCESS,message="Update task success")
            return redirect('tasks')
        except ValueError:
            return render(request,'tasks/editar.html',
            {   
                'task':task,
                'form':form,
                'error':"Error updating task"
            })

@login_required
def completed_task(request,task_id):
    task = get_object_or_404(Task,pk=task_id,user=request.user)
    if request.method=="POST":
        task.datecompleted = timezone.now()
        print(task)
        task.save()
        return redirect('tasks')

@login_required
def delete_task(request,task_id):
    task = get_object_or_404(Task,pk=task_id,user=request.user)
    if request.method=="POST":
        task.delete()
        return redirect('tasks') 


#Funcionalidad para registar usuario
def signup(request): 
    if request.method=='GET':
        return render(request,'signup.html',{'form':UserCreationForm})
    else:
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.create_user(username=request.POST['username'],
                password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('tasks')
            except IntegrityError:
                return render(request,'signup.html',{'form':UserCreationForm,'error':'El usuario ya existe'})
        return render(request,'signup.html',{'form':UserCreationForm,'error':'Man las contraseñan no son iguales'})
            
def signin(request):
    if request.method=="GET":
        return render(request,'signin.html',{'form':AuthenticationForm})
    else:
        user = authenticate(request,username=request.POST['username'],
                     password=request.POST['password'])
        #Comprabando s es válido el usuario
        if user is None :
             render(request,'signin.html',{
                 'form':AuthenticationForm,
                 'error':"El usuario y la contraseña es incorrecto"
            })
        else:
            login(request,user)
            return redirect('tasks') 
    

def cerrar_sesion(request):
    logout(request)
    return redirect('base')





    







        