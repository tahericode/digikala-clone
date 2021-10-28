from django.db import models
from shop.models import Product
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

#order class
class Order(models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE )
    first_name = models.CharField(_('نام'), max_length=50)
    last_name = models.CharField(_('نام خانوادگی'), max_length=50)
    email = models.EmailField(_('ایمیل'))
    address = models.CharField(_('ادرس'), max_length=250)
    postal_code = models.CharField(_('کدپستی'), max_length=20)
    city = models.CharField(_('شهر'), max_length=100)
    created = models.DateTimeField(_('تاریخ انتشار'), auto_now_add=True)
    updated = models.DateField(_('تاریخ بروزرسانی'), auto_now=True)
    paid = models.BooleanField(_('پرداختی'), default=False)

    # Order tracking
    accept_order = models.BooleanField(_('تایید سفارش'), default=False)
    prepare_order = models.BooleanField(_('آماده سازی سفارش'), default=False) 
    exit_processing_center = models.BooleanField(_('خروج از مرکز پردازش'),default=False)
    delivery_to_customer = models.BooleanField(_('تحویل به مشتری'), default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = _('سفارش')
        verbose_name_plural = _('سفارشات')

    def __str__(self):
        return 'Order {}'.format(self.id)

    # Total cost
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    # get detailPrivateMessages by id
    def get_absolute_url(self):
        return reverse('orders:detailOrderTracking', args=[self.id])
    


# OrderItem class
class OrderItem(models.Model):
    order = models.ForeignKey( Order, related_name='items', on_delete=models.CASCADE, verbose_name=_('سفارش'))
    product = models.ForeignKey( Product, related_name='order_items', on_delete=models.CASCADE, verbose_name=_('محضول'))
    price = models.DecimalField(_('قیمت'), max_digits=10, decimal_places=0)
    quantity = models.PositiveIntegerField(_('تعداد'), default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price*self.quantity