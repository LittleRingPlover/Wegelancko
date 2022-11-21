from django.shortcuts import render
from django.http import HttpResponse
from .models import Owner, Recipe, Comments


def index(request):
    return render(request, 'recipes/index.html')


def categories(request):
    recipes = Recipe.objects.all()
    categories = recipes.category_set.all()
    context = {'recipes': recipes}
    return render(request, 'recipes/categories.html', context)


def recipes():
    return HttpResponse("Tu będą przepisy należące do danej kategorii.")


def recipe():
    return HttpResponse("Tu będzie opis jednego przepisu.")
