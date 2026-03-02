from django.urls import path
from . import views

urlpatterns = [
    path('pagina_inicial', views.pagina_inicial_view, name = 'pagina_inicial')
]