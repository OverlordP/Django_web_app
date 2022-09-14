from unicodedata import name
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cartas3
# Create your views here.
def allCartas(request):
    cartas1 = Cartas3.objects.all()
    return render(request, 'cartas.html',{ "cartas" : cartas1})

def oneCarta(request,id):

    carta = get_object_or_404(Cartas3, id=id)
    return render(request, 'carta.html', { "carta" : carta})

def setCartas(request):
    return render(request, 'postCartas.html')

def postCartas(request):
    titulo = request.POST['titulo']
    nombre = request.POST['name']
    descripcion = request.POST['description']
    url = request.POST['Url']
    modelo = Cartas3(title = titulo, name= nombre, description= descripcion, Url = url)
    modelo.save()
    return redirect ('/cartas/')

def deleteCartas(request,id):
    carta= Cartas3.objects.get(id=id)
    carta.delete()
    return redirect ('/cartas/')

def updateCartas(request,id):
    carta = get_object_or_404(Cartas3, id=id)
    return render(request, 'updateCarta.html', {"carta": carta})

def updateCarta(request):
    
    titulo = request.POST['titulo']
    nombre = request.POST['name']
    descripcion = request.POST['description']
    url = request.POST['Url']
    modelo = Cartas3(id = request.POST['idt'],title = titulo, name= nombre, description= descripcion, Url = url)
    modelo.save()
    return redirect ('/cartas/')