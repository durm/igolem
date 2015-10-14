from django.db import models
from django.contrib.auth.models import User
from products.utils import *

class Proto(models.Model):

    name = models.CharField(max_length=512, blank=False, null=False)
    desc = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to="products", null=True, blank=True)
    thumb = models.ImageField(upload_to="products", null=True, blank=True)
    created_by = models.ForeignKey(User, related_name="+", blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    updated_by = models.ForeignKey(User, related_name="+", blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False, null=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class PageProto(models.Model):

    content = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True

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
        errors = []
        for node in tax.getchildren():
            name = node.get("name")
            try:
                category = Category(name=name, **kwargs)
                category.save()
                kw = kwargs.copy()
                kw["parent"] = category
                Category.store_from_taxonomy(node, **kw)
            except Exception as e:
                errors.append("{1} (Error: {0})".format(str(e), name))
        return errors
    
    @staticmethod
    def delete_all():
        categories = Category.objects.all()
        categories.delete()

class Product(Proto, PageProto):

    vendor = models.ForeignKey(Vendor, related_name="+", null=False, blank=False)
    categories = models.ManyToManyField(Category)
    
    external_link = models.URLField(null=True, blank=True)
    raw = models.TextField(blank=True, null=True)

    trade_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    retail_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    is_available_for_trade = models.BooleanField()
    is_available_for_retail = models.BooleanField()
    is_recommend_price = models.BooleanField()
    is_trade_by_order = models.BooleanField()
    is_new = models.BooleanField()
    is_special_price = models.BooleanField()

    def get_name(self):
        return "{0} {1}".format(self.vendor.name, self.name)

    @staticmethod
    def mark_all_as_unavailable():
        products = Product.objects.all()
        products.update(is_available_for_trade=False, is_available_for_retail=False)

    @staticmethod
    def store_from_price(file, **kwargs):
        errors = []
        transform_booleans = lambda d, k: d.setdefault(k, False) == "1"
        for prd in file.xpath(".//product"):
            try:
                kw = kwargs.copy()
                attribs = dict(prd.items())
                vendor, created = Vendor.objects.get_or_create(name=attribs["vendor"], **kw)
                del attribs['vendor']
                for key in ("is_available_for_trade", "is_available_for_retail", "is_recommend_price", "is_trade_by_order", "is_new", "is_special_price"):
                    transform_booleans(attribs, key)
                kw.update(attribs)
                product, created = Product.objects.get_or_create(vendor=vendor, name=attribs["name"], defaults=kw)
                if not created:
                    del kw['created_by'], kw['name']
                    for attr, value in kw.items(): 
                        setattr(product, attr, value)
                    product.save()
            except Exception as e:
                errors.append("{1} (Error: {0})".format(str(e), prd.get("raw")))
        return errors

    def update_content(self):
        if self.external_link is not None:
            self.content = get_external_desc(self.external_link)

    def update_image(self, f=None):
        if f is None :
            if self.external_link is not None:
                pass



class Page(Proto, PageProto):
    pass
