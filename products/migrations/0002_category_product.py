# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('desc', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+')),
                ('parent', models.ForeignKey(blank=True, to='products.Category', null=True)),
                ('updated_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('desc', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('photo', models.ImageField(blank=True, upload_to='products', null=True)),
                ('thumb', models.ImageField(blank=True, upload_to='products', null=True)),
                ('external_link', models.URLField(blank=True, null=True)),
                ('full_desc', models.TextField(blank=True, null=True)),
                ('trade_price', models.DecimalField(max_digits=12, blank=True, decimal_places=4, null=True)),
                ('retail_price', models.DecimalField(max_digits=12, blank=True, decimal_places=4, null=True)),
                ('is_available_for_trade', models.BooleanField()),
                ('is_available_for_retail', models.BooleanField()),
                ('is_recommend_price', models.BooleanField()),
                ('is_trade_by_order', models.BooleanField()),
                ('is_new', models.BooleanField()),
                ('is_special_price', models.BooleanField()),
                ('categories', models.ManyToManyField(to='products.Category')),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+')),
                ('updated_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+')),
                ('vendor', models.ForeignKey(to='products.Vendor', related_name='+')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
