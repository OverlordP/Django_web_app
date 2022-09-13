from django.shortcuts import render
from .models import Cartas3
# Create your views here.
def allCartas(request):
    cartas1 = Cartas3.objects.all()
    return render(request, 'cartas.html',{ "cartas" : cartas1})

def oneCarta(request,id):
    return render(request, 'carta.html')