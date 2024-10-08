from django.contrib import admin
from .models import Category
from .models import Product


# Register your models here.

# Below is to get the details in Admin panel
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description')
# admin.site.register(Category, CategoryAdmin)


admin.site.register(Category)
admin.site.register(Product)
