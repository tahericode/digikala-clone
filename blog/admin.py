from django.contrib import admin
from .models import Post, PostCategory, Comment
from jalali_date.admin import ModelAdminJalaliMixin
from jalali_date import datetime2jalali
# Register your models here.

#Register PostCategory model to admin page
@admin.register(PostCategory)
class CategoryAdmin(admin.ModelAdmin):
    # display with name and slug
    list_display = ['name', 'slug']
    # prepopulated slug with name
    prepopulated_fields = {'slug': ('name',)}
    # search with name
    search_fields = ['name']

# add Comment model to admin page
class CommentAdmin(admin.ModelAdmin):
    # display with user - post - get_created_jalai - active
    list_display = ['user', 'post', 'get_created_jalali', 'active']
    # filter with active - created - updated
    list_filter = ['active', 'created', 'updated']
    # search with user__username - post__title and body
    search_fields = ['user__username', 'post__title', 'body']

    # for jalali
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created).strftime('%Y/%m/%d _ %H:%M:%S')
    get_created_jalali.short_description = 'زمان ساخت'
    get_created_jalali.admin_order_field = 'created'

# To be placed PostAdmin inline
class CommentInline(admin.TabularInline):
    model = Comment

#Register Post model to admin page
@admin.register(Post)
class PostAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    # show title - slug - author - get_publish_jalali - status 
    list_display = ['title', 'slug', 'author', 'get_publish_jalali', 'status']
    # filter with status - created - publish - author
    list_filter = ['status', 'created', 'publish', 'author']
    # search with status - author__username - title - category__name
    search_fields = ['status', 'author__username', 'title', 'category__name']
    # prepopulated slug with title 
    prepopulated_fields = {'slug': ('title',)}
    # date_hierarchy with publish
    date_hierarchy = 'publish'
    # Commentline is PostAdmin inline
    inlines = [CommentInline]
    # for jalali
    def get_publish_jalali(self, obj):
    	return datetime2jalali(obj.publish).strftime('%Y/%m/%d _ %H:%M:%S')
    get_publish_jalali.short_description = 'تاریخ انتشار'
    get_publish_jalali.admin_order_field = 'publish'
 

