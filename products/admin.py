from django.contrib import admin

from products.models import *

admin.site.register(Vendor)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Page)
