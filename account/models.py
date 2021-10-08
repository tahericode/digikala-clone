from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE, verbose_name=_('کاربر'))
    date_of_birth = models.DateField(_('تاریخ تولد'), max_length=50, blank=True, null=True )
    photo = models.ImageField(_('عکس'), upload_to = 'users/%Y/%m/%d', blank = True , null = True)
    address = models.CharField(_('آدرس'), max_length=150)
    postal_code = models.PositiveIntegerField(_('کد پستی'), null = True, blank=True)
    city = models.CharField(_('شهر'), max_length=30)

    def __str__(self):
        return 'profile for user'.format(self.user.username)
    
    class Meta:
        verbose_name = _('پروفایل')
        verbose_name_plural = _('پروفایل')


