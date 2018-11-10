from django.shortcuts import render
from django.template import loader
from memes import models

# Create your views here.
from django.http import HttpResponse


def fresh(request):
    memes = models.Meme.objects.all()[:3]
    return render(request, 'memes/posts.html', {'memes': memes})

def upload(request):
    return render(request, 'memes/posts.html', {'memes':{}})