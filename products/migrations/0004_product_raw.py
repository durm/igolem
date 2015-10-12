# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20151010_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='raw',
            field=models.TextField(null=True, blank=True),
        ),
    ]
