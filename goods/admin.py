from django.contrib import admin
from .models import Categories, Goods
# Register your models here.


def capitalize_title(modeladmin, request, queryset):
    for model in queryset:
        model.name = model.name.capitalize()
        model.save()

capitalize_title.short_description = 'Нормализовать заголовок'

@admin.register(Goods)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'is_active')
    list_filter = ('is_active', )
    search_fields = ('name', )
    actions = [capitalize_title]

@admin.register(Categories)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_filter = ('is_active', )
    search_fields = ('name', )
    actions = [capitalize_title]
