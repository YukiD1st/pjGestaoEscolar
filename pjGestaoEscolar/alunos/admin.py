from django.contrib import admin

# Register your models here.
from .models import Aluno

class AlunoAdmin(admin.ModelAdmin):
    list_display = ['matricula', 'nome']
    search_fields = ['matricula', 'nome']

admin.site.register(Aluno, AlunoAdmin)