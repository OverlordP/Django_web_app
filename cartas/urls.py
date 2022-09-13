from django.urls import path

from cartas.views import *

urlpatterns = [
    path('', allCartas),
    path('<int:id>/', oneCarta),
]