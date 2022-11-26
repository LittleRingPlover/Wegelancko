from django.forms import ModelForm, Textarea
from .models import Owner, Tag, Recipe, Comments


class OwnerForm(ModelForm):
    class Meta:
        model = Owner
        fields = '__all__'
        labels = {
            'name': '',
            'website': '',
        }


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
        labels = {
            'title': '',
        }


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        labels = {
            'title': '',
            'content': '',
        }
        widgets = {
            'content': Textarea(attrs={'cols': 80, 'rows': 20})
        }


class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = '__all__'
        labels = {
            'content': '',
            'publication_date': '',
            'user': '',
        }
        widgets = {
            'content': Textarea(attrs={'cols': 80, 'rows': 20})
        }
