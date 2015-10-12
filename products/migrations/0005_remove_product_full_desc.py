# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_raw'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='full_desc',
        ),
    ]
