from django.contrib import admin

from .models import *

class ImageInlineAdmin(admin.TabularInline):
    model = Image
    fields = ('image', )
    max_num = 5

@admin.register(Products)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [ImageInlineAdmin,]

# Register your models here.
admin.site.register(Category)


