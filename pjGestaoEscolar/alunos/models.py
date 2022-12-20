from django.db import models

# Create your models here.
class Aluno(models.Model):
    matricula = models.TextField()
    nome = models.TextField()