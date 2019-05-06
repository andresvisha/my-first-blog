from django.contrib import admin
from .models import Post #Importamos el modelo que hemos creado.

admin.site.register(Post) #Registramos el modelo que creamos.
