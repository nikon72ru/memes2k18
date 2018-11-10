from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseRedirect
from memes import models
from django.http import HttpResponse
from django.core.serializers import json
from .forms import UploadFileForm
from memes.utils import Utils
from django.views.decorators.csrf import csrf_exempt

def fresh(request):
    cluster = models.Cluster.objects.filter(name = '0', type = 'text')
    memes = models.Meme.objects.filter(cluster_text = cluster)[:10]
    return render(request, 'memes/posts.html', {'memes': memes})

def upload(request):
    try:
        filter = request.GET.__getitem__('filter')
        pic_url = 'users_images/' + request.GET.__getitem__('source')
    except Exception as ex:
        filter = ''
        pic_url = ''
    memes = models.Meme.objects.all()[:3]
    return render(request, 'memes/upload.html', {'memes':memes, 'pic_url':pic_url})

def hot(request):
    memes = models.Meme.objects.all()[:1]
    return render(request, 'memes/posts.html', {'memes': memes})

def relevant(request):
    memes = models.Meme.objects.all()[:2]
    return render(request, 'memes/posts.html', {'memes': memes})

@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print(request)
        if True:
            Utils.handle_uploaded_file(request.FILES['image'])
            return HttpResponse('?filter=""&source='+request.FILES['image'].name)
    else:
        form = UploadFileForm()
    return HttpResponse("404")