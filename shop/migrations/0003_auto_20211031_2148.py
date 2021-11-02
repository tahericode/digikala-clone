# Generated by Django 2.2.15 on 2021-10-31 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20211031_2146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='meta_description_en',
            new_name='meta_description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='meta_title_en',
            new_name='meta_title',
        ),
        migrations.RemoveField(
            model_name='product',
            name='meta_description_fa',
        ),
        migrations.RemoveField(
            model_name='product',
            name='meta_title_fa',
        ),
    ]