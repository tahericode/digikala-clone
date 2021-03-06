from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from django.utils.translation import gettext_lazy as _
from translated_fields import TranslatedField
from ckeditor_uploader.fields import RichTextUploadingField

# Category class
class Category(models.Model):
    name =TranslatedField(  models.CharField(_('نام'), max_length=200, db_index=True) )
    slug = models.SlugField(_('اسلاگ'), max_length=200, db_index=True, unique=True)

    class Meta:
        verbose_name = _('دسته بندی')
        verbose_name_plural = _('دسته بندی ها')

    def __str__(self):
        return self.name
    # get product list by category
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

# product class
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.DO_NOTHING, verbose_name=_('دسته بندی'))
    name =TranslatedField(  models.CharField(_('نام'), max_length=200, db_index=True) )
    slug = models.SlugField(_('اسلاگ'), max_length=200, db_index=True)
    image = models.ImageField(_('عکس'), upload_to = 'products/%Y/%m/%d', blank = True)
    description =TranslatedField(  RichTextUploadingField(_('توضیحات')) )
    price = models.DecimalField(_('قیمت'), max_digits=10, decimal_places=0)
    stock = models.PositiveIntegerField(_('تعداد موجودی'))
    tags = TaggableManager(_('تگ ها'))
    available = models.BooleanField(_('فعال/غیر فعال'), default=True)
    created = models.DateTimeField(_('تاریخ انتشار'), auto_now_add=True)
    updated = models.DateField(_('تاریخ اپدیت'), auto_now=True)
    favorite = models.ManyToManyField(User, related_name='favorite', default=None, blank=True)


    #Seo fields
    meta_title =TranslatedField(models.CharField(_('meta_title'), max_length=350, blank=True, null=True) )
    meta_description =TranslatedField(models.TextField(_('meta_description'), max_length=350, blank=True, null=True) )
    meta_keywords =TranslatedField( models.TextField(_('meta_keywords'), max_length=350, blank=True, null=True) )
    alt_image =TranslatedField( models.TextField(_('alt_image'), max_length=350, blank=True, null=True) )


    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)
        verbose_name =_('محصول')
        verbose_name_plural = _('محصولات')

    def __str__(self):
        return self.name
    # get detailproduct by id, slug
    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug]) 



# comment class
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_comments', verbose_name=_('کاربر'))
    product = models.ForeignKey(Product,
                            on_delete=models.CASCADE,
                            related_name='comments', verbose_name=_('محصول'))

    name = models.CharField(_('نام'), max_length=80)
    email = models.EmailField(_('ایمیل'))
    body = models.TextField(_('متن پیام'))
    created = models.DateTimeField(_('تاریخ انتشار'),auto_now_add=True)
    updated = models.DateTimeField(_('تاریخ بروزرسانی'), auto_now=True)
    active = models.BooleanField(_('فعال/غیرفعال'), default=False)

    

    class Meta:
        ordering = ('created',)
        verbose_name = _('کامنت')
        verbose_name_plural = _('کامنت ها')


    
    def __str__(self):
        return f'Comment by {self.name} on {self.product}'

# productImaes for products    
class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='productImages')
    image = models.ImageField(_('عکس گالری'), upload_to = 'imagesProduct/%Y/%m/%d')

    class Meta:
        verbose_name = _('عکس های محصول')
        verbose_name_plural = _('عکس های محصولات')



