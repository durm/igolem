from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.template.context_processors import csrf
from products.models import Category
from products.parse_taxonomy import parse_taxonomy

def update_taxonomy(request):
    if request.method == 'GET':
        c = {}
        c.update(csrf(request))
        return render_to_response("update_taxonomy.html", c, context_instance=RequestContext(request))
    elif request.method == 'POST':
        print(parse_taxonomy(request.FILES['file']))
        return render("1")
