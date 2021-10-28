from django.contrib import admin
from . models import Profile
from jalali_date.admin import ModelAdminJalaliMixin
from jalali_date import datetime2jalali

# admin for Profile class
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # show user - date of birth - phto in display admin
    list_display = ['user', 'date_of_birth', 'photo']

    # for jalali
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.date_of_birth).strftime('%Y/%m/%d _ %H:%M:%S')
    get_created_jalali.short_description = 'تاریخ تولد'
    get_created_jalali.admin_order_field = 'date_of_birth'


