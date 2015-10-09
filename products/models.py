from django.db import models
from django.contrib.auth.models import User

class Proto(models.Model):

    name = models.CharField(max_length=512, blank=False, null=False)
    desc = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name="+", blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    updated_by = models.ForeignKey(User, related_name="+", blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False, null=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Vendor(Proto):
    pass

class Category(Proto):
    parent = models.ForeignKey('self', null=True, blank=True)

    def getchildren(self):
        return Category.objects.filter(parent=self)

    @staticmethod
    def get_roots():
        return Category.objects.filter(parent=None)

    @staticmethod
    def store_from_taxonomy(tax, **kwargs):
        for node in tax.getchildren():
            category = Category(name=node.get("name"), **kwargs)
            category.save()
            kw = kwargs.copy()
            kw["parent"] = category
            Category.store_from_taxonomy(node, **kw)

    @staticmethod
    def delete_all():
        categories = Category.objects.all()
        categories.delete()

class Product(Proto):
    
    vendor = models.ForeignKey(Vendor, related_name="+", null=False, blank=False)
    categories = models.ManyToManyField(Category)
    photo = models.ImageField(upload_to="products", null=True, blank=True)
    thumb = models.ImageField(upload_to="products", null=True, blank=True)
    external_link = models.URLField(null=True, blank=True)
    full_desc = models.TextField(blank=True, null=True)

    trade_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    retail_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    is_available_for_trade = models.BooleanField()
    is_available_for_retail = models.BooleanField()
    is_recommend_price = models.BooleanField()
    is_trade_by_order = models.BooleanField()
    is_new = models.BooleanField()
    is_special_price = models.BooleanField()
