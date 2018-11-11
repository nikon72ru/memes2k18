from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseRedirect
from memes import models
from django.http import HttpResponse
from django.core.serializers import json
from .forms import UploadFileForm
from memes.utils import Utils
from django.views.decorators.csrf import csrf_exempt
from memes.scripts.recognition import recognite_image_cluster
import requests
from memes.scripts.TextSearch import textSearch


def fresh(request):
    memes = Utils.getFresh(0)
    return render(request, 'memes/lenta.html', {'memes': memes})

def upload(request):
    clusters_name = []
    try:
        filter = request.GET.__getitem__('filter')
        clusters_name = filter.split(',')
        cluster_text = models.Cluster.objects.filter(name=clusters_name[0], type='text').last()
        if (len(clusters_name)>1):
            cluster_label = models.Cluster.objects.filter(name=clusters_name[1], type='tag').last()
        else:
            cluster_label = models.Cluster.objects.all()[0:0]
    except Exception as ex:
        filter = ''
        cluster_text = models.Cluster.objects.all()[0:0]
        cluster_label = models.Cluster.objects.all()[0:0]
    try:
        pic_url = 'users_images/' + request.GET.__getitem__('source')
    except:
        pic_url = ''
    return render(request, 'memes/upload.html', {'memes': Utils.getForFind(filter,0 ), 'pic_url':pic_url, 'cluster_text':cluster_text, 'cluster_label':cluster_label, 'has_filter':len(clusters_name)>0})

def hot(request):
    memes = Utils.getHottest(0)
    return render(request, 'memes/lenta.html', {'memes': memes})

def relevant(request):
    try:
        filter = request.GET.__getitem__('filter')
    except:
        filter = '-1'
    memes = Utils.getFromClusterLabel(filter, 0, 10)
    return render(request, 'memes/lenta.html', {'memes': memes})

@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print(request)
        if True:
            Utils.handle_uploaded_file(request.FILES['image'])
            res = recognite_image_cluster(request.FILES['image'].name)
            return HttpResponse('?filter='+str(res[0])+','+str(res[1])+'&source='+request.FILES['image'].name)
    else:
        form = UploadFileForm()
    return HttpResponse("404")

@csrf_exempt
def get_more(request):
    if request.method == 'POST':
        try:
            filter = request.GET.__getitem__('cluster')
        except:
            filter = '-1'
        if 'upload' in request.POST['type']:
            return render(request, 'memes/posts.html', {'memes': Utils.getForFind(request.POST['filter'],
                                                                                  request.POST['offset'])})
        elif 'fresh' in request.POST['type']:
            return render(request, 'memes/posts.html', {'memes': Utils.getFresh(request.POST['offset'])})
        elif 'hot' in request.POST['type']:
            return render(request, 'memes/posts.html', {'memes': Utils.getHottest(request.POST['offset'])})
        elif 'relevant' in request.POST['type']:
            return render(request, 'memes/posts.html', {'memes': Utils.getFromClusterLabel(request.POST['filter'], request.POST['offset'], 10)})

        return HttpResponse("404")


@csrf_exempt
def finder(request):
    if request.method == 'POST':
       text = request.POST['str']
       try:
           r = requests.get(text, allow_redirects=True)
           open('static/users_images/'+text.split('/')[-1], 'wb+').write(r.content)
           res = recognite_image_cluster(text.split('/')[-1])
           return HttpResponse('?filter=' + str(res[0]) + ',' + str(res[1]) + '&source=' +text.split('/')[-1])
       except:
           cluster_id = textSearch(text)
           return HttpResponse('?filter=%d' % cluster_id)





