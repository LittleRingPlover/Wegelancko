from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Owner, Recipe, Comments


def index(request):
    return render(request, 'recipes/index.html')


def categories(request, category_id):
    recipes = get_object_or_404(Recipe, category_id)
    for r in recipes:
        category = r.category
    context = {'recipes': recipes, 'category': category}
    return render(request, 'recipes/categories.html', context)


def recipes():
    return HttpResponse("Tu będą przepisy należące do danej kategorii.")


def recipe():
    return HttpResponse("Tu będzie opis jednego przepisu.")
