from django import forms
from .models import Owner, Category, Recipe, Comments, CATEGORY_CHOICES

choices = Category.objects.all().values_list('title', 'title')
choices_list = []
for item in choices:
    choices_list.append(item)


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


class RecipeForm(forms.ModelForm):
    title = forms.TextInput()
    preparation_time = forms.TextInput()
    servings = forms.TextInput()
    ingredients = forms.TextInput()
    content = forms.TextInput()

    class Meta:
        model = Recipe
        exclude = ['publication_date', 'edition_date', 'user', 'owner']
        labels = {
            'image': 'Dodaj zdjęcie jedzonka:',
            'title': '',
            'preparation_time': '',
            'servings': '',
            'ingredients': '',
            'content': '',
            'publication_date': '',
            'category': 'Wybierz kategorię:',
            'user': '',

        }

        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Nazwa przepisu'
                                            }),
            'preparation_time': forms.TextInput(attrs={'class': 'form-control',
                                                       'placeholder': 'Czas przygotowania'
                                                       }),
            'servings': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': 'Ilość porcji'
                                               }),
            'ingredients': forms.Textarea(attrs={'cols': 80, 'rows': 10,
                                                 'class': 'form-control',
                                                 'placeholder': 'Składniki'
                                                 }),
            'content': forms.Textarea(attrs={'cols': 80, 'rows': 20,
                                             'class': 'form-control',
                                             'placeholder': 'Treść przepisu'
                                             }),
            'category': forms.Select(choices=choices_list,
                                     attrs={'class': 'form-control'
                                            }),
            # 'owner': forms.TextInput(attrs={'class': 'form-control',
            #                                 'placeholder': 'Właściciel przepisu (skąd masz przepis?)'
            #                                 }),
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
