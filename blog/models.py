from typing import DefaultDict
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _
from translated_fields import TranslatedField



# Create PostCategory Model
class PostCategory(models.Model):
    name =TranslatedField( models.CharField(_('نام دسته بندی'), max_length=200, db_index=True, default='') )
    slug =models.SlugField(_('slug'), max_length=200, unique=True, default='')

    class Meta:
        verbose_name =  _('دسته بندی پست')
        verbose_name_plural = _('دسته بندی پست ها')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("blog:post_list_by_category", args=[self.slug])

# model manager (published product)
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

# Create Post Model
class Post(models.Model):
    # choises for status field
    STATUS_CHOICES = (
        ('draft', 'در انتظار'),
        ('published', 'منتشر شده'),
    )
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE, related_name='blogs', verbose_name=_('دسته بندی'))
    title =TranslatedField( models.CharField(_('عنوان'), max_length=250, default='') )
    slug = models.SlugField(_('slug'), max_length=250, unique_for_date='publish', default='')
    author =TranslatedField( models.CharField(_('نویسنده'), max_length=250, default='') )
    image = models.ImageField(_('عکس اصلی'), upload_to='blog/%Y/%m/%d', blank=True)
    short_description =TranslatedField( RichTextUploadingField(_('توضیحات مختصر'), blank=True, null=True,) )
    long_description =TranslatedField( RichTextUploadingField(_('توضیحات جامع'), blank=True, null=True) )
    publish = models.DateTimeField(_('تاریخ انتشار'), default=timezone.now) 
    created = models.DateTimeField(_('زمان ساخت'), auto_now_add=True)
    updated = models.DateTimeField(_('زمان به روز رسانی'), auto_now=True)
    status = models.CharField(_('وضعیت انتشار'), max_length=10, choices=STATUS_CHOICES, default='draft')
    #add model manager
    objects = models.Manager() # the default manager
    published = PublishedManager() # Our custom manager
    #Seo fields
    meta_title =TranslatedField( models.CharField(_('meta_title'), max_length=350, blank=True, null=True) )
    meta_description =TranslatedField( models.TextField(_('meta_description'), max_length=350, blank=True, null=True) )
    meta_keywords =TranslatedField( models.TextField(_('meta_keywords'), max_length=350, blank=True, null=True) )
    alt_image =TranslatedField( models.TextField(_('alt_image'), max_length=350, blank=True, null=True) )
    
    class Meta:
        verbose_name =  _('پست')
        verbose_name_plural = _('پست ها')
    
    def __str__(self):
        return self.title
    # get detailpost by year, month, day, slug
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

# Create Comment Model
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name=_('پست مورد نظر'))
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_comments', verbose_name=_('کاربر'))
    
    body = models.TextField(_('دیدگاه مورد نظر'))
    created = models.DateTimeField(_('زمان ساخت'), auto_now_add=True)
    updated = models.DateTimeField(_('زمان به روز رسانی'), auto_now=True)
    active = models.BooleanField(_('فعال بودن نمایش دیدگاه در سایت'), default=False)

    class Meta:
        ordering = ('created',)
        verbose_name =  _('دیدگاه های پست')
        verbose_name_plural = _('دیدگاه های پست ها')
    def __str__(self):
        return 'Comment by {} on {}'.format(self.user, self.post)