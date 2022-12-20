from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        usuario = request.POST.get("usuario")
        senha = request.POST.get("senha")
        user = authenticate(request, username=usuario, password=senha)
        if user is None:
            contexto = {"error" : "Usuario ou senha incorreto"}
            return render(request, "login.html", contexto)
        print("Gotcha")
        login(request, user)
        return redirect('/')
    return render(request, "login.html", {})

@login_required
def logout_view(request):
    logout(request)
    return redirect('/login')

def register_view(request):
    return render(request, "login.html", {})