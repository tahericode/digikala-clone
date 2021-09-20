from django.contrib import admin
from .models import Category, Product, Comment, ProductImages

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)

class ProductImagesInline(admin.TabularInline):
    model = ProductImages



class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'product', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


class CommentInline(admin.TabularInline):
    model = Comment


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated', 'category']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug':('name',)}
    inlines = [ProductImagesInline, CommentInline]
admin.site.register(Product, ProductAdmin)




