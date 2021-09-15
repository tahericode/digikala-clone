from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Question(models.Model):
    name = models.CharField(max_length=50, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(verbose_name='ایمیل')
    subject = models.CharField(max_length=500, null=False, verbose_name='موضوع')
    description = models.TextField(blank=True, null=True, verbose_name='پیام')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ارسال')

    class Meta:
        ordering = ('created',)
        verbose_name =  'سوال'
        verbose_name_plural = 'سوالات متداول'

    def __str__(self):
        return self.name


class ContactUs(models.Model):
    name = models.CharField(max_length=50, verbose_name= 'نام و نام خانوادگی')
    email = models.EmailField(verbose_name='ایمیل')
    tel = PhoneNumberField( null=False,verbose_name='شماره همراه')
    subject = models.CharField(max_length=500, null=False, verbose_name='موضوع')
    description = models.TextField( blank=True, null=True , verbose_name='توضیحات')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ارسال')
    updated = models.DateTimeField(auto_now=True, verbose_name='تاریخ به روز رسانی')

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'تماس با ما'

    def __str__(self):
        return self.name


