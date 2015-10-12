from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.template.context_processors import csrf
from products.models import Category, Product
from products.parse_taxonomy import parse_taxonomy
from xls.xlstoxml import xls_to_xml_by_fileobject
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

def update_from_file_form(request, **kwargs):
    kw = kwargs.copy()
    kw.update(csrf(request))
    return render_to_response("update_from_file.html", kw, context_instance=RequestContext(request))

def categories_processing(file, user):
    tax = parse_taxonomy(file)      
    Category.delete_all() 
    return Category.store_from_taxonomy(tax, parent=None, created_by=user, updated_by=user)

def products_processing(file, user):
    price = xls_to_xml_by_fileobject(file)
    Product.mark_all_as_unavailable()
    return Product.store_from_price(price, created_by=user, updated_by=user)

def update_from_file(request, title, processing, next):
    if request.method == 'GET':
        return update_from_file_form(request, title=title)
    elif request.method == 'POST':
        errors = processing(request.FILES['file'], request.user)
        if errors:
            return render_to_response("errors.html", {"errors": errors}, context_instance=RequestContext(request))
        return redirect(reverse(next))

@login_required
def update_taxonomy(request):
    return update_from_file(request, "Обновить рубрикацию", categories_processing, "update_taxonomy")

@login_required
def update_products(request):
    return update_from_file(request, "Обновить продукты", products_processing, "update_products")


