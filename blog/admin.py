from django.contrib import admin
from .models import Post, PostCategory, Comment
from jalali_date.admin import ModelAdminJalaliMixin
from jalali_date import datetime2jalali
# Register your models here.

#Register PostCategory model to admin page
@admin.register(PostCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


# add Comment model to admin page
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'get_created_jalali', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['user__username', 'post__title', 'body']

    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created).strftime('%Y/%m/%d _ %H:%M:%S')
    get_created_jalali.short_description = 'زمان ساخت'
    get_created_jalali.admin_order_field = 'created'



class CommentInline(admin.TabularInline):
    model = Comment




#Register Post model to admin page
@admin.register(Post)
class PostAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'get_publish_jalali', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['status', 'author__username', 'title', 'category__name']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'

    inlines = [CommentInline]

    def get_publish_jalali(self, obj):
    	return datetime2jalali(obj.publish).strftime('%Y/%m/%d _ %H:%M:%S')
    get_publish_jalali.short_description = 'تاریخ انتشار'
    get_publish_jalali.admin_order_field = 'publish'
 

