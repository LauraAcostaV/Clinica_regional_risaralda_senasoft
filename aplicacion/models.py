from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Usuario(models.Model):
	Usuario = models.CharField(max_length=20)
	Contraseña = models.CharField(max_length=20)

class Especialista(models.Model):
	nombre = models.CharField(max_length= 50, blank=False, null=False)
	apellidos = models.CharField(max_length=50, blank=False, null=False)
	documento_identidad = models.IntegerField(blank=False, null=False)
	correo = models.EmailField(blank=True, null=False)
	celular = models.CharField(max_length=15, blank=False, null=False)
	fechaNacimiento = models.DateField(blank=False)

	especialidades = (
		('Pe', 'Pediatra'),
		('Fa', 'Farmaceuta'),
		('UCI', 'Unidad de cuidados intensivos'),
		('Ge', 'Medico General')
	)
	especialidad = models.CharField(max_length=35, choices=especialidades, default='Ge')

	Created = models.DateTimeField(auto_now_add=True, blank=True)
	Modified = models.DateTimeField(auto_now=True, blank=True)

	def __str__(self):
		return '{0} {1}'.format(self.apellidos, self.nombre)

class Enfermeros(models.Model):
	nombre = models.CharField(max_length= 50, blank=False, null=False)
	apellidos = models.CharField(max_length=50, blank=False, null=False)
	documento_identidad = models.IntegerField(blank=False, null=False)
	correo = models.EmailField(blank=True, null=False)
	celular = models.CharField(max_length=15, blank=False, null=False)
	fechaNacimiento = models.DateField(blank=False)
	especialista = models.ForeignKey(Especialista, on_delete=models.CASCADE)

	Created = models.DateTimeField(auto_now_add=True, blank=True)
	Modified = models.DateTimeField(auto_now=True, blank=True)

	def __str__(self):
		return '{0} {1}'.format(self.apellidos, self.nombre)                                	
									
class Paciente(models.Model):
	nombre = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	
	TIPO_DOCUMENTO = (
		('CC', 'Cedula de Ciudadania'),
		('TI', 'Tarjeta de Identidad'),
		('CE', 'Cedula de Extrangeria')
	)

	tipo_documento = models.CharField(max_length=30, choices=TIPO_DOCUMENTO, default='CC')
	documento = models.IntegerField(blank=False, null=False)
	correo = models.EmailField(blank=False, null=False)
	celular = models.CharField(max_length=15, blank=False, null=False)
	fechaNacimiento = models.DateField(blank=False)
	especialidad = models.ForeignKey(Especialista, on_delete=models.CASCADE)
	enfermero = models.ForeignKey(Enfermeros, on_delete=models.CASCADE)
	
	Created = models.DateTimeField(auto_now_add=True, blank=True)
	Modified = models.DateTimeField(auto_now=True, blank=True)

	def __str__(self):
		return '{0} {1}'.format(self.apellidos, self.nombre)

class Turnos(models.Model):
	fecha_hora = models.DateTimeField(blank=False)
	especialista = models.OneToOneField(Especialista, on_delete=models.CASCADE)
	enfermero = models.OneToOneField(Enfermeros, on_delete=models.CASCADE)



