from django.shortcuts import render

# Create your views here.
def pagina_inicial_view(request):
    return render (request,'blog/pagina_inicial.html')