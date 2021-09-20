from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE, verbose_name='کاربر')
    date_of_birth = models.DateField(max_length=50, blank=True, null=True, verbose_name='تاریخ تولد')
    photo = models.ImageField(upload_to = 'users/%Y/%m/%d', blank = True , null = True, verbose_name='عکس')
    address = models.CharField(max_length=150, verbose_name='آدرس')
    postal_code = models.PositiveIntegerField(verbose_name='کد پستی', null = True, blank=True)
    city = models.CharField(max_length=30, verbose_name='شهر')

    def __str__(self):
        return 'profile for user'.format(self.user.username)
    
    class Meta:
        verbose_name = 'پروفایل'
        verbose_name_plural = 'پروفایل'


