from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from recipes.models import Owner, Recipe, Comments, Category


def index(request):
    categories = Category.objects.filter()
    first_recipe = Recipe.objects.order_by('-id')[0]
    second_recipe = Recipe.objects.order_by('-id')[1]
    third_recipe = Recipe.objects.order_by('-id')[2]
    context = {'categories': categories,
               'first_recipe': first_recipe,
               'second_recipe': second_recipe,
               'third_recipe': third_recipe,
               }
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
    return render(request, 'recipes/show_recipes.html', context)


def show_recipe(request, pk):
    recipe = get_object_or_404(Recipe, id=pk)
    context = {'recipe': recipe}
    return render(request, 'recipes/recipe_detail.html', context)


def add_recipe(request):
    return render(request, 'add_recipe.html')
