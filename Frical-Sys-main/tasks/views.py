from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Budget

from .forms import BudgetForm

# Create your views here.

'''Esta función maneja el registro de usuarios.
Si la solicitud es una petición GET, muestra el formulario de registro (signup.html).
Si la solicitud es una petición POST, verifica que las contraseñas coincidan y crea un nuevo usuario utilizando el modelo User de Django. Luego, inicia sesión con el nuevo usuario y redirige a la página de tareas (tasks).'''
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'signup.html', {"form": UserCreationForm, "error": "Passwords did not match."})

'''Estas funciones manejan la visualización de las tareas pendientes y las tareas completadas respectivamente.
Filtran las tareas en función del usuario actual y si la fecha de finalización es nula o no.
Renderizan las plantillas tasks.html con las tareas correspondientes.'''
@login_required
def tasks(request):
    tasks = Budget.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'tasks.html', {"tasks": tasks})

@login_required
def tasks2(request):
    tasks = Budget.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'tasks2.html', {"tasks": tasks})



@login_required
def tasks_completed(request):
    tasks = Budget.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'tasks2.html', {"tasks": tasks})

'''Esta función maneja la creación de una nueva tarea.
Si la solicitud es una petición GET, muestra el formulario para crear una nueva tarea (create_task.html).
Si la solicitud es una petición POST, valida el formulario TaskForm, asigna el usuario actual a la tarea y la guarda en la base de datos. Luego, redirige a la página de tareas (tasks).'''
@login_required
def create_task(request):
    if request.method == "GET":
        return render(request, 'create_task.html', {"form": BudgetForm})
    else:
        try:
            form = BudgetForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_task.html', {"form": BudgetForm, "error": "Error creating task."})

'''Esta función renderiza la plantilla home.html, que es la página de inicio.'''
def home(request):
    return render(request, 'home.html')

'''Esta función realiza el cierre de sesión del usuario y redirige a la página de inicio (home).'''
@login_required
def signout(request):
    logout(request)
    return redirect('home')

'''Esta función maneja el inicio de sesión de usuarios existentes.
Si la solicitud es una petición GET, muestra el formulario de inicio de sesión (signin.html).
Si la solicitud es una petición POST, autentica al usuario utilizando las credenciales proporcionadas y, si son válidas, inicia sesión y redirige a la página de tareas (tasks).'''
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('tasks')
'''Esta función maneja la visualización y actualización de una tarea específica.
Si la solicitud es una petición GET, obtiene la tarea correspondiente utilizando su ID y comprueba si pertenece al usuario actual. Luego, muestra la plantilla task_detail.html con la tarea y un formulario TaskForm para editarla.
Si la solicitud es una petición POST, actualiza la tarea con los datos del formulario y redirige a la página de tareas (tasks).'''
@login_required
def task_detail(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Budget, pk=task_id, user=request.user)
        form = BudgetForm(instance=task)
        return render(request, 'task_detail.html', {'task': task, 'form': form})
    else:
        try:
            task = get_object_or_404(Budget, pk=task_id, user=request.user)
            form = BudgetForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'task_detail.html', {'task': task, 'form': form, 'error': 'Error updating task.'})

@login_required
def task_detail2(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Budget, pk=task_id, user=request.user)
        form = BudgetForm(instance=task)
        return render(request, 'task_detail2.html', {'task': task, 'form': form})
    else:
        try:
            task = get_object_or_404(Budget, pk=task_id, user=request.user)
            form = BudgetForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'task_detail2.html', {'task': task, 'form': form, 'error': 'Error updating task.'})






'''Esta función marca una tarea como completada.
Obtiene la tarea correspondiente utilizando su ID y comprueba si pertenece al usuario actual.
Si la solicitud es una petición POST, actualiza la fecha de finalización de la tarea a la fecha y hora actuales y guarda los cambios. Luego, redirige a la página de tareas (tasks).'''
@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Budget, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tasks')
    


'''Esta función elimina una tarea.
Obtiene la tarea correspondiente utilizando su ID y comprueba si pertenece al usuario actual.
Si la solicitud es una petición POST, elimina la tarea de la base de datos y redirige a la página de tareas (tasks).'''
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Budget, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
    


    # tasks = Budget.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    # return render(request, 'taskviews.html', {"tasks": tasks})

