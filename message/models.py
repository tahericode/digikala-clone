from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings


# model manager
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class PublicMassages(models.Model):
    STATUS_CHOICES = (
        ('draft', 'در انتظار'),
        ('published', 'منتشر شده'),
    )
    section           = models.CharField(('پیام از بخش'), max_length=250)
    subject           = models.CharField(('موضوع'), max_length=250)
    short_description = models.TextField(('توضیحات مختصر'), blank=True, null=True)
    long_description  = RichTextUploadingField(('توضیحات جامع'), blank=True, null=True)
    publish           = models.DateField(('تاریخ انتشار'), default=timezone.now)
    created           = models.DateTimeField(('زمان ساخت'), auto_now_add=True, blank=True, null=True)
    updated           = models.DateTimeField(('زمان به روز رسانی'), auto_now=True, blank=True, null=True)
    status            = models.CharField(('وضعیت انتشار'), max_length=10, choices=STATUS_CHOICES, default='draft')
    #add model manager
    objects           = models.Manager() # the default manager
    published         = PublishedManager() # Our custom manager
    
    class Meta:
        ordering = ('-publish',)
        verbose_name =  ('پیام های عمومی')
        verbose_name_plural = ('پیام های عمومی')
    
    def _str_(self):
        return self.subject


class PrivateMassages(models.Model):
    STATUS_CHOICES = (
        ('draft', 'در انتظار'),
        ('published', 'منتشر شده'),
    )
    user              = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='کاربر')
    section           = models.CharField(('پیام از بخش'), max_length=250)
    subject           = models.CharField(('موضوع'), max_length=250)
    short_description = models.TextField(('توضیحات مختصر'), blank=True, null=True)
    long_description  = RichTextUploadingField(('توضیحات جامع'), blank=True, null=True)
    publish           = models.DateField(('تاریخ انتشار'), default=timezone.now)
    created           = models.DateTimeField(('زمان ساخت'), auto_now_add=True, blank=True, null=True)
    updated           = models.DateTimeField(('زمان به روز رسانی'), auto_now=True, blank=True, null=True)
    status            = models.CharField(('وضعیت انتشار'), max_length=10, choices=STATUS_CHOICES, default='draft')
    #add model manager
    objects           = models.Manager() # the default manager
    published         = PublishedManager() # Our custom manager
    
    class Meta:
        ordering = ('-publish',)
        verbose_name =  ('پیام های خصوصی')
        verbose_name_plural = ('پیام های خصوصی')
    
    def _str_(self):
        return self.subject