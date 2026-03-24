from django.urls import path
from . import views

urlpatterns = [
    path('fenomenologia', views.fenomenologia_view, name = 'pagina_inicial'),
    path('artigos', views.article_list, name='article_list'),
]