from django.urls import path
from . import views

urlpatterns = [
    path('hamburguesa/', views.HamburguesasApiView.as_view(), name='Hamburguesas'),
    path('hamburguesa/<id>', views.HamburguesaApiView.as_view(), name='Hamburguesa'),
    path('ingrediente/', views.IngredientesApiView.as_view(), name='Ingredientes'),
    path('ingrediente/<id>', views.IngredienteApiView.as_view(), name='Ingrediente'),
    path('hamburguesa/<id_h>/ingrediente/<id_i>', views.HamburguesasIngredientesApiView.as_view(), name='Hamburguesa e Ingrediente')
    
]