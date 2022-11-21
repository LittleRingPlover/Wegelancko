from django.db import models


class Owner(models.Model):
    """Owner of the recipe."""
    name = models.CharField(max_length=100)
    website = models.URLField(null=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """Recipe added by the user."""
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    edition_date = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    class Category(models.TextChoices):
        BREAKFAST = 'BR'
        APPETIZERS = 'AP'
        SOUPS = 'SO'
        MAIN_DISHES = 'MD'
        DESSERTS = 'DE'
        CATEGORY = [
            (BREAKFAST, 'Śniadania'),
            (APPETIZERS, 'Przystawki'),
            (SOUPS, 'Zupy'),
            (MAIN_DISHES, 'Dania główne'),
            (DESSERTS, 'Ciasta i desery'),
        ]
        category = models.CharField(
            max_length=20,
            choices=CATEGORY)

    def __str__(self):
        return self.title


class Comments(models.Model):
    """Comments of recipes written by users."""
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    edition_date = models.DateTimeField(auto_now=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.content # jeszcze do zmiany, damy tu usera
