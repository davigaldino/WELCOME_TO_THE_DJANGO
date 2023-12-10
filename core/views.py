from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade, numero1, numero2):
    soma = numero1 + numero2
    return HttpResponse('<h1>Hello {} de {} anos</h1><p></p> <h3>A soma é igual a {}</h3>'.format(nome, idade, soma))