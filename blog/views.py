from django.shortcuts import render
from .models import Article

# Create your views here.
def fenomenologia_view(request):
    return render (request,'blog/fenomenologia.html')

def article_list(request):
    articles = Article.objects.order_by('-created_at')
    return render(request, 'blog/artigos.html', {'articles': articles})