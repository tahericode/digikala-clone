from shop.views import product_detail
from django.db import models

from shop.models import Product

class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='نام ')
    last_name = models.CharField(max_length=50, verbose_name='نام خانوادگی')
    email = models.EmailField(verbose_name='ایمیل')
    address = models.CharField(max_length=250, verbose_name='ادرس')
    postal_code = models.CharField(max_length=20, verbose_name='کدپستی')
    city = models.CharField(max_length=100, verbose_name='شهر')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')
    updated = models.DateField(auto_now=True, verbose_name='تاریخ بروزرسانی')
    paid = models.BooleanField(default=False, verbose_name='پرداختی')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات'

    def __str__(self):
        return 'Order {}'.format(self.id)


    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())



class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name='سفارش')
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE, verbose_name='محضول')
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='قیمت')
    quantity = models.PositiveIntegerField(default=1, verbose_name='تعداد')

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price*self.quantity