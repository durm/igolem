from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.template.context_processors import csrf
from products.models import Category
from products.parse_taxonomy import parse_taxonomy
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

@login_required
def update_taxonomy(request):
    if request.method == 'GET':
        roots = Category.get_roots()
        c = {
            "roots": roots
        }
        c.update(csrf(request))
        return render_to_response("update_taxonomy.html", c, context_instance=RequestContext(request))
    elif request.method == 'POST':
        tax = parse_taxonomy(request.FILES['file'])      
        Category.delete_all() 
        Category.store_from_taxonomy(tax, parent=None, created_by=request.user, updated_by=request.user)
        return redirect(reverse("update_taxonomy"))
