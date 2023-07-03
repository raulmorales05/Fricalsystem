from django.contrib import admin
from .models import Budget
'''Importaciones de módulos:

Se importa el módulo admin del paquete django.contrib de Django.
Se importa el modelo Task de tu aplicación.

El comentario # Register your models here.:
Es un comentario que indica que a continuación se registrarán los modelos en el administrador de Django.

La clase TaskAdmin(admin.ModelAdmin):
Esta clase define una configuración personalizada para el modelo "Task" en el administrador.
Hereda de la clase admin.ModelAdmin, que es una clase base en Django para personalizar la representación y el comportamiento de los modelos en el administrador.

El atributo readonly_fields:
Este atributo define qué campos del modelo "Task" deben ser solo de lectura en el administrador.
En este caso, se establece como ('created', ), lo que significa que el campo "created" del modelo "Task" será solo de lectura en el administrador.

La línea admin.site.register(Task, TaskAdmin):
Esta línea registra el modelo "Task" en el administrador de Django.
Utiliza la función register() del objeto admin.site para registrar el modelo "Task".
También se proporciona la clase TaskAdmin como argumento, lo que indica que se utilizará la configuración personalizada definida en esa clase para el modelo "Task" en el administrador.

En resumen, este código registra el modelo "Task" en el administrador de Django y proporciona una configuración personalizada para ese modelo. La configuración personalizada establece el 
campo "created" como solo de lectura en el administrador. Esto permite controlar qué campos son editables y cuáles son solo de lectura al trabajar con objetos del modelo "Task" en la interfaz 
de administración de Django.'''

# Register your models here.
class BudgetAdmin(admin.ModelAdmin):
    readonly_fields = ('created', )

admin.site.register(Budget, BudgetAdmin)