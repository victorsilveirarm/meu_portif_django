from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Bem-vindo ao meu portfólio!</h1><p>Projeto Django funcionando 😎</p>")
