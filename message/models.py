from django.conf.urls import url
from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.utils.translation import gettext_lazy as _


# model manager
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class PublicMassages(models.Model):
    STATUS_CHOICES = (
        ('draft', _('در انتظار')),
        ('published', _('منتشر شده')),
    )
    section           = models.CharField(_('پیام از بخش'), max_length=250)
    subject           = models.CharField(_('موضوع'), max_length=250)
    short_description = models.TextField(_('توضیحات مختصر'), blank=True, null=True)
    long_description  = RichTextUploadingField(_('توضیحات جامع'), blank=True, null=True)
    publish           = models.DateField(_('تاریخ انتشار'), default=timezone.now)
    created           = models.DateTimeField(_('زمان ساخت'), auto_now_add=True, blank=True, null=True)
    updated           = models.DateTimeField(_('زمان به روز رسانی'), auto_now=True, blank=True, null=True)
    status            = models.CharField(_('وضعیت انتشار'), max_length=10, choices=STATUS_CHOICES, default='draft')
    #add model manager
    objects           = models.Manager() # the default manager
    published         = PublishedManager() # Our custom manager


    
    
    class Meta:
        ordering = ('-publish',)
        verbose_name =  _('پیام های عمومی')
        verbose_name_plural = _('پیام های عمومی')
    
    def _str_(self):
        return self.subject
    
    def get_absolute_url(self):
        return reverse('message:detailPublicMessages', args=[self.id])


class PrivateMassages(models.Model):
    STATUS_CHOICES = (
        ('draft', _('در انتظار')),
        ('published', _('منتشر شده')),
    )
    user              = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('کاربر'))
    section           = models.CharField(_('پیام از بخش'), max_length=250)
    subject           = models.CharField(_('موضوع'), max_length=250)
    short_description = models.TextField(_('توضیحات مختصر'), blank=True, null=True)
    long_description  = RichTextUploadingField(_('توضیحات جامع'), blank=True, null=True)
    publish           = models.DateField(_('تاریخ انتشار'), default=timezone.now)
    created           = models.DateTimeField(_('زمان ساخت'), auto_now_add=True, blank=True, null=True)
    updated           = models.DateTimeField(_('زمان به روز رسانی'), auto_now=True, blank=True, null=True)
    status            = models.CharField(_('وضعیت انتشار'), max_length=10, choices=STATUS_CHOICES, default='draft')
    #add model manager
    objects           = models.Manager() # the default manager
    published         = PublishedManager() # Our custom manager
    
    class Meta:
        ordering = ('-publish',)
        verbose_name =  _('پیام های خصوصی')
        verbose_name_plural = _('پیام های خصوصی')
    
    def _str_(self):
        return self.subject

    def get_absolute_url(self):
        return reverse('message:detailPrivateMessages', args=[self.id])