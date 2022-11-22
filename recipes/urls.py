from django.urls import path
from . import views

app_name = 'recipes'


urlpatterns = [
    path('', views.index, name='index'),
    path('tag/<int:tag_id>', views.show_recipes, name='recipes'),
    path('recipe/<int:recipe_id>/', views.show_recipe, name='recipe'),

]
