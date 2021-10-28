from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
#create model for Coupon
class Coupon(models.Model):
    code = models.CharField(_('کد تخفیف'), max_length=50,
                            unique=True)
    valid_from = models.DateTimeField(_('از تاریخ'))
    valid_to = models.DateTimeField(_('تا تاریخ'))
    discount = models.IntegerField(_('مقدار تخفیف(به درصد)'),
                                validators=[MinValueValidator(0),
                                MaxValueValidator(100)])
    active = models.BooleanField(_('فعال/غیر فعال'))
    def __str__(self):
        return self.code

    class Meta:
        verbose_name = _('تخفیف')
        verbose_name_plural = _('تخفیف ها')
