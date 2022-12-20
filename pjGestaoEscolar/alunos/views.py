from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Aluno

# Create your views here.
@login_required
def alunos_view(request):
    # devolve lista de todos os alunos/objetos
    list_queryset = Aluno.objects.all()
    contexto = {
        "titulo": "Listagem de Alunos",
        "lista_alunos": list_queryset,
    }
    return render(request, "alunos.html", context=contexto)

#POST request
@login_required
def aluno_search_detail_view(request):
    query = None
    contexto = {}
    try:
        query = request.POST.get("matricula")

        # pegar aluno/object pelo campo matricula
        al = Aluno.objects.get(matricula=query)

        contexto = {
            "nome_aluno": al.nome,
            "matricula_aluno": al.matricula,
            "titulo": al.nome,
        }
    except:
        query = None

    return render(request, "aluno.html", context=contexto)

#GET request
@login_required
def aluno_detail_view(request, matr):

    # pegar aluno/object pelo campo matricula
    al = Aluno.objects.get(matricula = matr)

    contexto = {
        "nome_aluno":al.nome,
        "matricula_aluno":al.matricula,
        "titulo": al.nome,
    }

    return render(request, "aluno.html", context=contexto)