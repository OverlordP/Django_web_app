from django.urls import path

from cartas.views import *

urlpatterns = [
    path('', allCartas, name="cartas"),
    path('form/', setCartas ,name="forms"),
    path('<int:id>/', oneCarta),
    path('forms/', postCartas, name="setforms"),
    path('delete/<int:id>/', deleteCartas, name="deletecarta"),
    path('update/<int:id>/', updateCartas, name="updatecarta"),
    path('formsid/', updateCarta, name="updateCartaid"),
]