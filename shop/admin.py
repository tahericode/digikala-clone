from django.contrib import admin
from .models import Category, Product, Comment, ProductImages
# for Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = [ 'slug']
admin.site.register(Category,CategoryAdmin)

# To be placed ProductAdmin inline
class ProductImagesInline(admin.TabularInline):
    model = ProductImages

# for Comment
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'product', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')

# To be placed ProductAdmin inline
class CommentInline(admin.TabularInline):
    model = Comment


class ProductAdmin(admin.ModelAdmin):
    list_display = [ 'slug', 'category', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated', 'category']
    list_editable = ['price', 'stock', 'available']
    # Commentline & ProductImagesInline  is ProductAdmin inline
    inlines = [ProductImagesInline, CommentInline]
admin.site.register(Product, ProductAdmin)




