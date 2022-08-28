from django.shortcuts import render

# Create your views here.
from .models import Directores, Peliculas, Genero

def index(request):

    #objetos totales
    num_peliculas= Peliculas.objects.all().count()
    peliculas= Peliculas.objects.all()
    directores= Directores.objects.all().count()
    director=Directores.objects.all()
    genero=Genero.objects.all()
    generos=Genero.objects.all().count()

    #objetos totales con un filtro
    directores_jubilados= Directores.objects.filter(estado='a').count()


    #obtenemos los datos que queremos pasar a la vista
    return render(
        request,
        'index.html',
        context={        
        'num_peliculas': num_peliculas,
        'directores' : directores,
        'directores_jubilados': directores_jubilados,
        'director': director,
        'peliculas' : peliculas, 
        'genero' : genero,
        'generos': generos
        }
    )
