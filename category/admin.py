from django.contrib import admin
from .models import Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug' : ('category_name',)}  #This will automatically fill the slug field.
    list_display = ['category_name', 'slug']
admin.site.register(Category, CategoryAdmin)


