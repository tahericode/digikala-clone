from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin
from jalali_date import datetime2jalali
# Register your
from .import models
# for PublicMessage 
@admin.register(models.PublicMassages)
class PublicMessagesAdmin(admin.ModelAdmin):
    # display section and subject
    list_display = ['section', 'subject']
    # for jalali
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created).strftime('%Y/%m/%d _ %H:%M:%S')
    get_created_jalali.short_description = 'زمان ساخت'
    get_created_jalali.admin_order_field = 'created'

# for privateMessages
@admin.register(models.PrivateMassages)
class PrivateMessagesAdmin(admin.ModelAdmin):
    # display section and subject
    list_display = ['section', 'subject']
    # for jalaly
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created).strftime('%Y/%m/%d _ %H:%M:%S')
    get_created_jalali.short_description = 'زمان ساخت'
    get_created_jalali.admin_order_field = 'created'