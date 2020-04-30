from django.shortcuts import render
from django.views import generic

# Create your views here.

def siteapp(request):
    args = {}
    text = "hello world"
    args['mytext'] = text
    return render(request, 'siteapp/index.html', args)
