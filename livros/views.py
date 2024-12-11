from django.shortcuts import render
from livros.models import Livro

def index(request):
    livros = Livro.objects.all()
    return render(request, 'index.html', {'livros': livros})