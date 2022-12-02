from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from recipes.models import Owner, Recipe, Comments, Category


def index(request):
    categories = Category.objects.filter()
    context = {'categories': categories}
    return render(request, 'recipes/index.html', context)


def home(request):
    return render(request, 'recipes/home.html')


# def show_recipes(request, tag_id):
#     tag = get_object_or_404(Tag, id=tag_id)
#     recipes = tag.recipe_set.all()
#     context = {'tag': tag, 'recipes': recipes, }
#     return render(request, 'recipes/recipes.html', context)

def show_recipes(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'recipes/recipes.html', context)


def show_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    category = recipe.category.all()
    context = {'recipe': recipe, 'category': category}
    return render(request, 'recipes/recipe.html', context)


def add_recipe(request):
    return render(request, 'add_recipe.html')
