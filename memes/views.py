from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse


def fresh(request):
    template = loader.get_template('memes/posts.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def upload(request):
    template = loader.get_template('memes/upload.html')
    context = {
    }
    return HttpResponse(template.render(context, request))