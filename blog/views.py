from django.shortcuts import render

# Create your views here.
def fenomenologia_view(request):
    return render (request,'blog/fenomenologia.html')