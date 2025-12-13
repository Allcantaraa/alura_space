from django.shortcuts import render
from usuarios.forms import LoginForms, CadastroForms
# Create your views here.

def login(request) :
    
    form_login = LoginForms()
    
    return render(request, 'usuario/login.html', {'form': form_login})

def cadastro(request) :
    
    form_cadastro = CadastroForms()
    
    return render(request, 'usuario/cadastro.html', {'form': form_cadastro})