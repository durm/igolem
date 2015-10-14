from django.conf.urls import patterns, url
from products.views import *

urlpatterns = patterns('',
    url(r'^update_taxonomy/$', update_taxonomy, name="update_taxonomy"),
    url(r'^update_products/$', update_products, name="update_products"),
    url(r'^product(?P<num>[0-9]+)/$', product_page, name="product_page"),
    url(r'^category(?P<num>[0-9]+)/$', category_page, name="category_page"),
)
