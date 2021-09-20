from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Coupon(models.Model):
    code = models.CharField(max_length=50,
                            unique=True, verbose_name='کد تخفیف')
    valid_from = models.DateTimeField(verbose_name='از تاریخ')
    valid_to = models.DateTimeField(verbose_name='تا تاریخ')
    discount = models.IntegerField(
                                validators=[MinValueValidator(0),
                                MaxValueValidator(100)], verbose_name='مقدار تخفیف(به درصد)')
    active = models.BooleanField(verbose_name='فعال/غیر فعال')
    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'تخفیف'
        verbose_name_plural = 'تخفیف ها'
