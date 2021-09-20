# Generated by Django 2.2.15 on 2021-09-19 06:08

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210918_0947'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'دسته بندی', 'verbose_name_plural': 'دسته بندی ها'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('created',), 'verbose_name': 'کامنت', 'verbose_name_plural': 'کامنت ها'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-created',), 'verbose_name': 'محصول', 'verbose_name_plural': 'محصولات'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=200, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=200, unique=True, verbose_name='اسلاگ'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=False, verbose_name='فعال/غیرفعال'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(verbose_name='متن پیام'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=80, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='shop.Product', verbose_name='محصول'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی'),
        ),
        migrations.AlterField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=True, verbose_name='فعال/غیر فعال'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='products', to='shop.Category', verbose_name='دسته بندی'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d', verbose_name='عکس'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(db_index=True, max_length=200, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=10, verbose_name='قیمت'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=200, verbose_name='اسلاگ'),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.PositiveIntegerField(verbose_name='تعداد موجودی'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='تگ ها'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated',
            field=models.DateField(auto_now=True, verbose_name='تاریخ اپدیت'),
        ),
    ]
