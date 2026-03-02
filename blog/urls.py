from django.urls import path
from . import views

urlpatterns = [
    path('fenomenologia', views.fenomenologia_view, name = 'pagina_inicial')
]