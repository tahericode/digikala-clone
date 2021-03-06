# Generated by Django 2.2.15 on 2021-11-01 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20211030_1306'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='alt_image',
            new_name='alt_image_en',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='meta_description',
            new_name='meta_description_en',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='meta_keywords',
            new_name='meta_keywords_en',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='meta_title',
            new_name='meta_title_en',
        ),
        migrations.AddField(
            model_name='post',
            name='alt_image_fa',
            field=models.TextField(blank=True, max_length=350, null=True, verbose_name='alt_image'),
        ),
        migrations.AddField(
            model_name='post',
            name='meta_description_fa',
            field=models.TextField(blank=True, max_length=350, null=True, verbose_name='meta_description'),
        ),
        migrations.AddField(
            model_name='post',
            name='meta_keywords_fa',
            field=models.TextField(blank=True, max_length=350, null=True, verbose_name='meta_keywords'),
        ),
        migrations.AddField(
            model_name='post',
            name='meta_title_fa',
            field=models.CharField(blank=True, max_length=350, null=True, verbose_name='meta_title'),
        ),
    ]
