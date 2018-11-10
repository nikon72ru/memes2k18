from django.shortcuts import render
from django.template import loader
from memes import models

# Create your views here.
from django.http import HttpResponse


def fresh(request):
    memes = models.Meme.objects.all()
    return render(request, 'memes/post_list.html', {'memes': memes})

def upload(request):
    template = loader.get_template('memes/upload.html')
    context = {
    }
    return HttpResponse(template.render(context, request))