from django.urls import path
from . import views

app_name = 'recipes'


urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.categories, name='categories'),
    path('recipes/', views.recipes, name='recipes'),
    path('recipes/<int:pk>/', views.recipe, name='recipe'),

]
