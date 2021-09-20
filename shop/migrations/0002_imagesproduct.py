# Generated by Django 2.2.15 on 2021-09-18 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagesProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='imagesProduct/%Y/%m/%d', verbose_name='عکس گالری')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product')),
            ],
            options={
                'verbose_name': 'عکس های محصول',
                'verbose_name_plural': 'عکس های محصولات',
            },
        ),
    ]