from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django_registration.forms import User
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from recipes.models import Owner, Recipe, Comments, Category
from .forms import RecipeForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q


def index(request):
    category = request.GET.get('category')
    if category is None:
        recipes = Recipe.objects.order_by('-publication_date').filter()
    else:
        recipes = Recipe.objects.filter(category__title=category)

    # recipe = Recipe.objects.all()
    # if Recipe.objects.filter().exists():
    #     first_recipe = Recipe.objects.order_by('-id')[0]
    #     second_recipe = Recipe.objects.order_by('-id')[1]
    #     third_recipe = Recipe.objects.order_by('-id')[2]
    # else:
    #     print('W bazie danych nie ma jeszcze przepisów. Dodaj je!')
    first_recipe = Recipe.objects.order_by('-id')[0]
    second_recipe = Recipe.objects.order_by('-id')[1]
    third_recipe = Recipe.objects.order_by('-id')[2]

    categories = Category.objects.all()

    context = {
               'recipes': recipes,
               'categories': categories,
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
    recipes = Recipe.objects.order_by('-publication_date')
    paginator = Paginator(recipes, 6)
    page_number = request.GET.get('page')

    try:
        recipes = paginator.page(page_number)
    except PageNotAnInteger:
        recipes = paginator.page(1)
    except EmptyPage:
        recipes = paginator.page(paginator.num_pages)

    categories = Category.objects.all()
    context = {'recipes': recipes, 'categories': categories}
    return render(request, 'recipes/show_recipes.html', context)


@login_required
def show_my_recipes(request):
    my_recipes = Recipe.objects.filter(user=request.user).order_by('-publication_date')
    paginator = Paginator(my_recipes, 6)
    page_number = request.GET.get('page')

    try:
        my_recipes = paginator.page(page_number)
    except PageNotAnInteger:
        my_recipes = paginator.page(1)
    except EmptyPage:
        my_recipes = paginator.page(paginator.num_pages)

    categories = Category.objects.all()
    context = {'my_recipes': my_recipes, 'categories': categories}
    return render(request, 'recipes/show_my_recipes.html', context)


def show_recipe(request, pk):
    recipe = get_object_or_404(Recipe, id=pk)
    context = {'recipe': recipe}
    return render(request, 'recipes/recipe_detail.html', context)


def add_recipe(request):

    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)

        if form.is_valid():
            new_recipe = form.save(commit=False)
            new_recipe.user = request.user
            new_recipe.save()

            return redirect('recipes:show_recipes')
    else:
        form = RecipeForm()

    context = {'form': form}
    return render(request, 'recipes/add_recipe.html', context)


def update_recipe(request, pk):
    recipe = Recipe.objects.get(id=pk)

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            updated_recipe = form.save(commit=False)
            updated_recipe.user = request.user
            updated_recipe.save()
            return redirect('recipes:show_recipe', pk=pk)
    else:
        form = RecipeForm(instance=recipe)

    context = {'recipe': recipe, 'form': form}
    return render(request, 'recipes/update_recipe.html', context)


class RecipeDelete(LoginRequiredMixin, DeleteView):
    model = Recipe
    context_object_name = 'recipe'
    success_url = reverse_lazy('recipes:show_recipes')


def search_recipe(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            recipes = Recipe.objects.filter(title__icontains=query)

            context = {'recipes': recipes}
            return render(request, 'recipes/search_recipe.html', context)
        else:
            print("Brak elementów spełniających kryteria wyszukiwania...")
            return render(request, 'recipes/search_recipe.html', {})
