from django.contrib import admin

# Register your models here.
from .models import Directores, Genero, Peliculas
admin.site.register(Directores)
admin.site.register(Genero)
admin.site.register(Peliculas)