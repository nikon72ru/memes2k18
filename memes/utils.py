import os
from random import randint

from memes import models
from django.db.models import Q

class Utils:
    def getHottest(count):
        firstCount = int(count*0.2)
        secondCount = int(count*0.3)
        counts = [count-firstCount-secondCount, secondCount, firstCount]
        pictures = []
        clusters = models.Cluster.objects.order_by('-requests').all()[:3]
        for cluster in clusters:
            pctrs = models.Meme.objects.filter(Q(cluster_text_id=cluster.id) | Q(cluster_label_id=cluster.id))[:counts[1]]
            for pic in pctrs:
                pictures.append(pic.image_url)

        return pictures

    def handle_uploaded_file(f):
        if not os.path.exists(os.path.dirname('static/users_images/'+f.name)):
            try:
                os.makedirs(os.path.dirname('static/users_images/'+f.name))
            except OSError as exc:  # Guard against race condition
                    raise

        with open('static/users_images/'+f.name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
