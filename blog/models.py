from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model

# Create your models here.

class Categoria(models.Model):
	nombre = models.CharField("Nombre", max_length=255)
	slug = models.SlugField("Slug", max_length=255)
	active = models.BooleanField("Activo", default=True)
	created_at = models.DateTimeField("Creado el", auto_now_add=True)
	updated_at = models.DateTimeField("Actualizado el", auto_now=True)

	class Meta:
		verbose_name='Categoría'
		verbose_name_plural = 'Categorías'
		ordering = ['-created_at']

	def __str__(self):
		return self.nombre

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.nombre)
		super(Categoria, self).save(*args, **kwargs)

class Color(models.Model):
	nombre = models.CharField(max_length=255)

	def __str__(self):
		return self.nombre


class Entrada(models.Model):
	titulo = models.CharField(max_length=300)
	slug = models.SlugField("Slug", max_length=255)
	contenido = RichTextField(
			'Contenido',
			help_text='Contenido de la página',
			blank=True
		)
	etiqueta = models.ForeignKey(Categoria)
	colores = models.ForeignKey(Color)
	active = models.BooleanField("Activo", default=True)
	created_at = models.DateTimeField("Creado el", auto_now_add=True)
	updated_at = models.DateTimeField("Actualizado el", auto_now=True)

	def __str__(self):
		return self.titulo

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.titulo)
		super(Entrada, self).save(*args, **kwargs)

	class Meta:
		verbose_name='Entrada'
		verbose_name_plural = 'Entradas'
		ordering = ['-created_at']

class Document(models.Model):
    descripcion = models.CharField(max_length=255, blank=True)
    titulo = models.CharField(max_length=300)
    documento = models.FileField(upload_to='static/documents/')
    imagen_pdf = models.FileField(upload_to='static/imagenes_pdf/')
    subido_el = models.DateTimeField(auto_now_add=True)


class Perfil_user(models.Model):
	age = models.CharField(max_length=100, blank=True)
	cellphone = models.CharField(max_length=100, blank=True)
	address = models.CharField(max_length=100, blank=True)
	job_info = models.CharField(max_length=100, blank=True)
	education = models.CharField(max_length=100, blank=True)
	biography = models.CharField(max_length=300, blank=True)
	social_network = models.CharField(max_length=100, blank=True)
	avatar_image = models.FileField(upload_to='static/avatar/', blank=True)

"""class Perfil(models.Model):
    user = models.ForeignKey(User, unique=True)
    biografia = RichTextField(
            'biografia',
            help_text='Biografia del Perfil',
            blank=True
        )
    direccion = models.CharField("direccion",max_length=300)
    estado = models.CharField("estado",max_length=300)
    profesion = models.CharField("profesion",max_length=300)
    trabajo = models.CharField("trabajo",max_length=300)
    telefono = models.CharField("telefono",max_length=300)
    email = models.CharField("email",max_length=300)
    facebook = models.CharField("redes sociales",max_length=300)
    twitter = models.CharField("redes sociales",max_length=300)
    area_agricola = models.CharField("actividad agricola",max_length=300)
    avatar = models.FileField(upload_to='static/avatar/',blank=True)
    is_human = models.BooleanField()
 
    def __unicode__(self):
        return self.user"""