from django.conf.urls import patterns, url
from products.views import *

urlpatterns = patterns('',
    url(r'^update_taxonomy/$', update_taxonomy, name="update_taxonomy"),
    url(r'^update_products/$', update_products, name="update_products"),
)
