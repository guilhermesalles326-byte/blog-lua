from django.db import models

# Create your models here.
from django.db import models

class Article(models.Model):
    title = models.CharField("Título", max_length=200)
    slug = models.SlugField(unique=True)
    summary = models.TextField("Resumo", blank=True)
    image = models.ImageField("Imagem de capa", upload_to='articles/', blank=True, null=True)
    content = models.TextField("Conteúdo")
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title