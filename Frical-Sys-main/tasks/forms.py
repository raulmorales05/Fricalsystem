from django.forms import ModelForm
from .models import Budget
'''Importaciones de módulos:
Se importan los módulos necesarios de Django, incluyendo ModelForm del módulo forms y el modelo Task de tu aplicación.

La clase TaskForm(ModelForm):
Esta clase define un formulario de modelo llamado "TaskForm".
Hereda de la clase ModelForm, que es una clase base en Django para crear formularios basados en modelos.

La clase interna Meta:
La clase Meta se utiliza para proporcionar metadatos adicionales al formulario.
En este caso, se especifica el modelo asociado al formulario utilizando el atributo model = Task. Esto indica que el formulario se basará en el modelo "Task".
El atributo fields define qué campos del modelo se incluirán en el formulario. En este caso, los campos incluidos son 'title', 'description' y 'important'.

En resumen, el formulario "TaskForm" se utiliza para crear un formulario que representa los campos del modelo "Task" ('title', 'description' y 'important'). 
Este formulario facilita la creación, edición y validación de objetos "Task" en las vistas de Django. Al utilizar este formulario, no es necesario crear campos manualmente,
ya que se generan automáticamente según el modelo asociado. Esto ahorra tiempo y facilita la creación de formularios coherentes con los modelos de tu aplicación.'''

class BudgetForm(ModelForm):
    class Meta:
        model = Budget
        fields = ['title', 'description', 'important', 'company', 'name', 'email', 'service_description', 'quantity', 'unit_price', 'total_price', 'payment_method', 'offer_validity', 'delivery_time', 'note']
        