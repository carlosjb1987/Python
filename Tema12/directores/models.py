from django.db import models
import uuid

# Create your models here.

class Genero(models.Model):
    genero=models.CharField(max_length= 30)

    def __str__(self):
        return self.genero

class Directores(models.Model):
    nombre=models.CharField(max_length= 30, help_text="Pon el nombre del director")

    estado= (
        ('a', 'Activo'),
        ('p', 'Parado'),
        ('j', 'Jubilado'),
    )
    
    estado=models.CharField(max_length=1, choices=estado, blank=True, default='a', help_text='Se encuenta activo, parado o jubilado')
    def __str__(self):
        return self.nombre

class Peliculas(models.Model):
    id = models. UUIDField(primary_key=True, default=uuid.uuid4)
    titulo=models.CharField(max_length= 100, help_text="Pon el nombre de la película")
    descripcion=models.TextField(max_length= 500, help_text="Escribe una breve descripción de la película")
    director= models.ForeignKey('Directores', on_delete=models.SET_NULL, null=True)
    genero= models.ManyToManyField(Genero)

    def __str__(self):
        return self.titulo