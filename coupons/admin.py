from django.contrib import admin
from .models import Coupon

#register Coupon Admin
@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    # display with code - valid_form - valid-to - discount - active
    list_display = ['code', 'valid_from', 'valid_to',
                    'discount', 'active']
    # filter by active - valid_form and valid_to
    list_filter = ['active', 'valid_from', 'valid_to']
    # search fields by code
    search_fields = ['code']
