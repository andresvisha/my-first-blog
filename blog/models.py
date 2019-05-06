from django.db import models
from django.utils import timezone

class Post(models.Model): 
#Class nos dice que estamos definiendo un objeto.
#Post es el nombre de nuestro modelo
#models.Model indica que es un modelo de Django, asi se guarda en la base de datos.

#Definimos las propiedades:
	#ForeignKey: define una relacion con otro modelo.
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	#CharField: define un texto con numero limitado de caracteres.
	title = models.CharField(max_length=200)
	#TextField: texto largo sin limite.
	text = models.TextField()
	#DateTimeField: fecha y hora.
	created_date = models.DateTimeField(
		default = timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)

	#Def: es una funcion/metodo
	#Publis es el nombre del metodo
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title #Retornamos el titulo, un string.