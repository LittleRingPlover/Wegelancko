from django.contrib import admin
from django.utils.html import format_html
from recipes.models import Owner, Recipe, Comments, Category, User
# Register your models here.


class CommentsInline(admin.StackedInline):
    model = Comments


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'user')
    list_filter = ('owner', 'user')
    search_fields = ('title', 'owner__name', 'user')
    inlines = [
        CommentsInline,
    ]


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'publication_date', 'recipe')
    list_filter = ('user', 'publication_date', 'recipe')
    search_fields = ('user', 'content', 'publication_date', 'recipe')


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_url')
    search_fields = ('name',)

    def show_url(self, obj):
        if obj.website is not None:
            return format_html(f'<a href="{obj.website}" target="_blank">{obj.website}</a>')
        else:
            return ''


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Owner, OwnerAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Category, CategoryAdmin)
