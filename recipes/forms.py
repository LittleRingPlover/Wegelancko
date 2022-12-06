from django import forms
from .models import Owner, Category, Recipe, Comments, CATEGORY_CHOICES


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = '__all__'
        labels = {
            'name': '',
            'website': '',
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        # labels = {
        #     'title': 'Kategoria',
        # }
        # widgets = {
        #     'title': forms.Select(choices=CATEGORY_CHOICES)
        # }


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        labels = {
            'title': 'Nazwa',
            'content': 'Treść',
        }

        category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), to_field_name='title')
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'preparation_time': forms.TextInput(attrs={'class': 'form-control'}),
            'servings': forms.TextInput(attrs={'class': 'form-control'}),
            'ingredients': forms.Textarea(attrs={'cols': 80, 'rows': 10, 'class': 'form-control'}),
            'content': forms.Textarea(attrs={'cols': 80, 'rows': 20, 'class': 'form-control'}),
            'publication_date': forms.TextInput(attrs={'class': 'form-control'}),
            'owner': forms.TextInput(attrs={'class': 'form-control'}),
            'user': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = '__all__'
        labels = {
            'content': '',
            'publication_date': '',
            'user': '',
        }
        widgets = {
            'content': forms.Textarea(attrs={'cols': 80, 'rows': 20})
        }
