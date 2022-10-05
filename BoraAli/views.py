from django.shortcuts import redirect, render
from BoraAli.models import Autor, Livro

# Create your views here.

def home(request):
    return render(request, 'BoraAli/home.html')


def autor(request):
    autores = Autor.objects.all()

    context


