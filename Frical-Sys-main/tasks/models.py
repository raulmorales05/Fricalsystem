from django.db import models
from django.contrib.auth.models import User

# Create your models here.
'''Importaciones de módulos:
Se importan los módulos necesarios de Django, incluyendo models y User del módulo contrib.auth.models.

La clase Task(models.Model):
Esta clase define el modelo "Task" que representa una tarea en el sistema.
Hereda de la clase models.Model, que es la clase base para todos los modelos en Django.

Atributos del modelo:

title: Es un campo de tipo CharField que representa el título de la tarea. Tiene una longitud máxima de 200 caracteres.
description: Es un campo de tipo TextField que representa la descripción de la tarea. Tiene una longitud máxima de 1000 caracteres.
created: Es un campo de tipo DateTimeField que registra la fecha y hora de creación de la tarea. Se establece automáticamente en la fecha y hora actual cuando se crea una instancia de la tarea.
datecompleted: Es un campo de tipo DateTimeField que registra la fecha y hora en la que se completó la tarea. Puede tener un valor nulo (null=True) o estar en blanco (blank=True) si la tarea aún no se ha completado.
important: Es un campo de tipo BooleanField que indica si la tarea es importante o no. Por defecto, se establece en False.
user: Es un campo de tipo ForeignKey que establece una relación con el modelo User de Django. Indica qué usuario está asociado con la tarea. Se utiliza el argumento on_delete=models.CASCADE para especificar que si se elimina un usuario, también se eliminarán todas las tareas asociadas a ese usuario.

El método __str__(self):
Este método define la representación en cadena de texto de una instancia de la clase Task. Devuelve una cadena que muestra el título de la tarea y el nombre de usuario del usuario asociado a la tarea.'''

from django.db import models

class Budget(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Campos adicionales para el presupuesto
    company = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    service_description = models.TextField(max_length=1000)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=200)
    offer_validity = models.CharField(max_length=200)
    delivery_time = models.CharField(max_length=200)
    note = models.TextField(blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.unit_price
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title + ' - ' + self.user.username
