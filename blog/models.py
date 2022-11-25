from datetime import datetime

from django.db import models

# Create your models here.

from django.db import models
from django.db.models import TextField
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    autor = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    conteudo = TextField()
    # conteudo = RichTextUploadingField()
    # imagem_capa = models.ImageField(null=True, blank=True, upload_to='static/blog/')
    data_publicacao = models.DateTimeField(default=datetime.now())
    # data_publicacao = models.DateTimeField(timezone.now())

    # def __str__(self):
    #     return self.titulo