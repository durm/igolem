# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0002_category_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=512)),
                ('desc', models.TextField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, upload_to='products', null=True)),
                ('thumb', models.ImageField(blank=True, upload_to='products', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+')),
                ('updated_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='category',
            name='photo',
            field=models.ImageField(blank=True, upload_to='products', null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='thumb',
            field=models.ImageField(blank=True, upload_to='products', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='photo',
            field=models.ImageField(blank=True, upload_to='products', null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='thumb',
            field=models.ImageField(blank=True, upload_to='products', null=True),
        ),
    ]
