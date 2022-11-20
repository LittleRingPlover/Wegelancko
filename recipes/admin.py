from django.contrib import admin
from django.utils.html import format_html
from recipes.models import Owner, Recipe, Comments
# Register your models here.


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'owner')
    list_filter = ('category', 'owner')
    search_fields = ('title', 'category', 'owner__name')


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('content', 'publication_date', 'recipe')
    list_filter = ('publication_date', 'recipe')
    search_fields = ('content', 'publication_date', 'recipe')


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_url')
    search_fields = ('name',)

    def show_url(self, obj):
        if obj.website is not None:
            return format_html(f'<a href="{obj.website}" target="_blank">{obj.website}</a>')
        else:
            return ''


admin.site.register(Owner, OwnerAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Comments, CommentsAdmin)
