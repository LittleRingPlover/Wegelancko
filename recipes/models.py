from django.db import models
from django.contrib.auth.models import User


class Owner(models.Model):
    """Owner of the recipe."""
    name = models.CharField(max_length=100)
    website = models.URLField(null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    objects = None
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Recipe(models.Model):
    """Recipe added by the user."""
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    edition_date = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comments(models.Model):
    """Comments of recipes written by registration."""
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    edition_date = models.DateTimeField(auto_now=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.content} - {self.user}"
