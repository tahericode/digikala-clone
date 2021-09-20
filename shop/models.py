from django.db import models
from django.db.models.fields.files import ImageField
from django.urls import reverse
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='نام')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='اسلاگ')

    class Meta:
        ordering = ('name',)
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.DO_NOTHING, verbose_name='دسته بندی')
    name = models.CharField(max_length=200, db_index=True, verbose_name='نام')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='اسلاگ')
    image = models.ImageField(upload_to = 'products/%Y/%m/%d', blank = True, verbose_name='عکس')
    description = RichTextField(verbose_name='توضیحات')
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='قیمت')
    stock = models.PositiveIntegerField(verbose_name='تعداد موجودی')
    tags = TaggableManager(verbose_name='تگ ها')
    available = models.BooleanField(default=True, verbose_name='فعال/غیر فعال')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')
    updated = models.DateField(auto_now=True, verbose_name='تاریخ اپدیت')

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug]) 




class Comment(models.Model):
    product = models.ForeignKey(Product,
                            on_delete=models.CASCADE,
                            related_name='comments', verbose_name='محصول')

    name = models.CharField(max_length=80, verbose_name='نام')
    email = models.EmailField(verbose_name='ایمیل')
    body = models.TextField(verbose_name='متن پیام')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')
    updated = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')
    active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')

    class Meta:
        ordering = ('created',)
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'


    
    def __str__(self):
        return f'Comment by {self.name} on {self.product}'

    
class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='productImages')
    image = models.ImageField(upload_to = 'imagesProduct/%Y/%m/%d', verbose_name='عکس گالری')

    class Meta:
        verbose_name = 'عکس های محصول'
        verbose_name_plural = 'عکس های محصولات'



