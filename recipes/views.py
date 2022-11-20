from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'recipes/index.html')


def categories():
    return HttpResponse("Tu będą kategorie posiłków.")


def recipes():
    return HttpResponse("Tu będą przepisy należące do danej kategorii.")


def recipe():
    return HttpResponse("Tu będzie opis jednego przepisu.")
