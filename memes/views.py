from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.serializers import json
from .forms import UploadFileForm
from memes.utils import Utils
from django.views.decorators.csrf import csrf_exempt

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