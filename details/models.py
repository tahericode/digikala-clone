from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

class Question(models.Model):
    name = models.CharField(_('نام و نام خانوادگی'), max_length=50)
    email = models.EmailField(_('ایمیل'))
    subject = models.CharField(_('موضوع'), max_length=500, null=False)
    description = models.TextField(_('پیام'), blank=True, null=True)
    created = models.DateTimeField(_('تاریخ ارسال'), auto_now_add=True)

    class Meta:
        ordering = ('created',)
        verbose_name =  _('سوال')
        verbose_name_plural = _('سوالات متداول')

    def __str__(self):
        return self.name


class ContactUs(models.Model):
    name = models.CharField(_('نام و نام خانوادگی'), max_length=50)
    email = models.EmailField(_('ایمیل'))
    tel = PhoneNumberField( _('شماره همراه'), null=False)
    subject = models.CharField(_('موضوع'), max_length=500, null=False)
    description = models.TextField(_('توضیحات'), blank=True, null=True )
    created = models.DateTimeField(_('تاریخ ارسال'), auto_now_add=True)
    updated = models.DateTimeField(_('تاریخ به روز رسانی'), auto_now=True)

    class Meta:
        verbose_name = _('تماس با ما')
        verbose_name_plural = _('تماس با ما')

    def __str__(self):
        return self.name


