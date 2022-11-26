from django.urls import path, re_path
from . import views

app_name = 'recipes'


urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('tag/<int:tag_id>', views.show_recipes, name='recipes'),
    path('recipe/<int:recipe_id>/', views.show_recipe, name='recipe'),
    path('recipe/add-recipe/', views.add_recipe, name='add_recipe'),

]
