from django.apps import AppConfig

'''Importación de módulos:
Se importa el módulo AppConfig del paquete django.apps de Django.

La clase TasksConfig(AppConfig):
Esta clase define la configuración de la aplicación "tasks".
Hereda de la clase AppConfig, que es una clase base en Django para configurar las aplicaciones.

Atributos de la clase:
default_auto_field: Este atributo especifica el tipo de campo automático utilizado para las claves primarias de los modelos en la aplicación.
En este caso, se establece como 'django.db.models.BigAutoField', que es un campo autoincremental de gran tamaño.
name: Este atributo especifica el nombre de la aplicación. En este caso, se establece como 'tasks'.
La configuración de la aplicación se utiliza para definir diferentes configuraciones específicas de la aplicación, como el tipo de campo automático utilizado para las claves primarias. 
Al definir una configuración de aplicación personalizada, puedes personalizar aún más el comportamiento y las características de tu aplicación de Django.'''
class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks'
