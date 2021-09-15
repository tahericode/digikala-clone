from django.contrib import admin
from . import models
class OrderItemInline(admin.TabularInline):
    model = models.OrderItem
    raw_id_fields =['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]


admin.site.register(models.Order, OrderAdmin) 
