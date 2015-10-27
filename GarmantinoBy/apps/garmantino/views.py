from django.shortcuts import render

from django.shortcuts import render, render_to_response
from django.template import RequestContext

def index(request):
    context = RequestContext(request, {})
    return render(request, 'index.html', context)

def catalogue(request):
    context = RequestContext(request, {})
    return render(request, 'catalogue.html', context)

def item(request, item_id):
    context = RequestContext(request, {'item_id': item_id})
    return render(request, 'item.html', context)
