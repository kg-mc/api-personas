#import path
from django.urls import path

from . import views

app_name = 'personas'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:persona_id>/results/', views.results, name='results'),
    path('id/<int:persona_id>/', views.results),
    path('dni/<str:dni>/', views.get_for_dni, name='get_for_dni'),
    path('resultados/', views.resultados, name='resultados'),
]
