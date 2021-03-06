# Generated by Django 2.2.15 on 2021-10-31 17:29

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(db_index=True, max_length=200, verbose_name='نام')),
                ('name_fa', models.CharField(db_index=True, max_length=200, verbose_name='نام')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='اسلاگ')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(db_index=True, max_length=200, verbose_name='نام')),
                ('name_fa', models.CharField(db_index=True, max_length=200, verbose_name='نام')),
                ('slug', models.SlugField(max_length=200, verbose_name='اسلاگ')),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d', verbose_name='عکس')),
                ('description_en', ckeditor.fields.RichTextField(verbose_name='توضیحات')),
                ('description_fa', ckeditor.fields.RichTextField(verbose_name='توضیحات')),
                ('price', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='قیمت')),
                ('stock', models.PositiveIntegerField(verbose_name='تعداد موجودی')),
                ('available', models.BooleanField(default=True, verbose_name='فعال/غیر فعال')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')),
                ('updated', models.DateField(auto_now=True, verbose_name='تاریخ اپدیت')),
                ('meta_title_en', models.CharField(blank=True, max_length=350, null=True, verbose_name='meta_title')),
                ('meta_title_fa', models.CharField(blank=True, max_length=350, null=True, verbose_name='meta_title')),
                ('meta_description_en', models.TextField(blank=True, max_length=350, null=True, verbose_name='meta_description')),
                ('meta_description_fa', models.TextField(blank=True, max_length=350, null=True, verbose_name='meta_description')),
                ('meta_keywords', models.TextField(blank=True, max_length=350, null=True, verbose_name='meta_keywords')),
                ('alt_image', models.TextField(blank=True, max_length=350, null=True, verbose_name='alt_image')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='products', to='shop.Category', verbose_name='دسته بندی')),
                ('favorite', models.ManyToManyField(blank=True, default=None, related_name='favorite', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='تگ ها')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
                'ordering': ('-created',),
                'index_together': {('id', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='imagesProduct/%Y/%m/%d', verbose_name='عکس گالری')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productImages', to='shop.Product')),
            ],
            options={
                'verbose_name': 'عکس های محصول',
                'verbose_name_plural': 'عکس های محصولات',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='نام')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('body', models.TextField(verbose_name='متن پیام')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
                ('active', models.BooleanField(default=False, verbose_name='فعال/غیرفعال')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='shop.Product', verbose_name='محصول')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_comments', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'کامنت',
                'verbose_name_plural': 'کامنت ها',
                'ordering': ('created',),
            },
        ),
    ]
