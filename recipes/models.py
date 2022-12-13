from django.db import models
from django.contrib.auth.models import User


class Owner(models.Model):
    """Owner of the recipe."""
    name = models.CharField(max_length=100)
    website = models.URLField(null=True)

    def __str__(self):
        return self.name


CATEGORY_CHOICES = [
    ('1', 'Śniadania'),
    ('2', 'Przystawki'),
    ('3', 'Zupy'),
    ('4', 'Dania główne'),
    ('5', 'Ciasta i desery'),
]


class Category(models.Model):
    objects = None
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Recipe(models.Model):
    """Recipe added by the user."""
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=200)
    preparation_time = models.CharField(max_length=20)
    servings = models.CharField(max_length=200)
    ingredients = models.TextField()
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    edition_date = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Comments(models.Model):
    """Comments of recipes written by registration."""
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    edition_date = models.DateTimeField(auto_now=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.content} - {self.user}"
