from django.contrib import admin
from . import models
import csv
import datetime
from django.http import HttpResponse
from django.urls import reverse
from django.utils.safestring import mark_safe
from jalali_date.admin import ModelAdminJalaliMixin
from jalali_date import datetime2jalali


# for export to csv
def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    # to indicate that the HTTP response contains an attached file
    content_disposition = 'attachment; filename={opts.verbose_name}.csv'
    # For response that content type = text/csv
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = content_disposition
    writer = csv.writer(response)

    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    # Write a first row with header information
    writer.writerow([field.verbose_name for field in fields])
    # Write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response
export_to_csv.short_description = 'Export to CSV'



# To be placed OrderAdmin inline
class OrderItemInline(admin.TabularInline):
    model = models.OrderItem
    raw_id_fields =['product']


# for order_pdf
def order_pdf(obj):
    # url for get pdf using id
    url = reverse('orders:admin_order_pdf', args=[obj.id])
    return mark_safe(f'<a href="{url}">PDF</a>')
order_pdf.short_description = 'Invoice'

# Order Admin
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address', 'postal_code', 'city', order_pdf]
    list_filter = ['paid', 'created', 'updated']
    # OrderItemInline is OrderAdmin inline
    inlines = [OrderItemInline]
    actions = [export_to_csv]
    # for jalali
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created).strftime('%Y/%m/%d _ %H:%M:%S')
    get_created_jalali.short_description = 'زمان ساخت'
    get_created_jalali.admin_order_field = 'created'
admin.site.register(models.Order, OrderAdmin) 
