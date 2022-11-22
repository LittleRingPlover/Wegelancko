from django.contrib import admin
from django.utils.html import format_html
from recipes.models import Owner, Recipe, Comments, Tag, User
# Register your models here.


class CommentsInline(admin.StackedInline):
    model = Comments


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner',)
    list_filter = ('owner',)
    search_fields = ('title', 'owner__name',)
    inlines = [
        CommentsInline,
    ]


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


class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Owner, OwnerAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Tag, TagAdmin)
