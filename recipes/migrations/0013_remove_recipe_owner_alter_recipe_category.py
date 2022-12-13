# Generated by Django 4.1.3 on 2022-12-06 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0012_remove_recipe_category_recipe_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='owner',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.CharField(choices=[('1', 'Śniadania'), ('2', 'Przystawki'), ('3', 'Zupy'), ('4', 'Dania główne'), ('5', 'Ciasta i desery')], max_length=50),
        ),
    ]
