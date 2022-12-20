from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from alunos.models import Aluno

@login_required
def home_view(request, *args, **kwargs):
    """
    al_obj = Aluno()
    al_obj.matricula = "080200"
    al_obj.nome = "Lucas"
    al_obj.matricula = "010160"
    al_obj.nome = "Matheus"
    al_obj.matricula = "180052"
    al_obj.nome = "Andreia"
    al_obj.save()"""

    context = {
        "titulo": "Página inicial",
    }
    return render(request, "home-view.html", context)