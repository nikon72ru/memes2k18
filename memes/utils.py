import os
from random import randint

from memes import models
from django.db.models import Q
from itertools import chain
from memes.scripts.recognition import recognite_image_cluster

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

    def getFresh(time):
        return models.Meme.objects.order_by('-created_at').filter(created_at__lte=time)[:10]

    def getFromClusterText(id, offset, count):
        cl = models.Cluster.objects.filter(name=id).last()
        return models.Meme.objects.order_by('-created_at').filter(cluster_text=cl)[offset:count]

    def getFromClusterLabel(id, offset, count):
        cl = models.Cluster.objects.filter(name=id).last()
        return models.Meme.objects.order_by('-created_at').filter(cluster_label=cl)[offset:count]

    def getForFind(filter, offset):
        clusters = filter.split(',')
        fromtext = Utils.getFromClusterText(clusters[0], offset, 3)
        fromlabel = Utils.getFromClusterLabel(clusters[1], offset, 7)
        return list(chain(fromlabel, fromtext))

    def getForFindAll(path):
        res = recognite_image_cluster(path)
        fromtext = Utils.getFromClusterText(res[0], 0, 9999)
        fromlabel = Utils.getFromClusterLabel(res[1], 0, 9999)
        return list(chain(fromlabel, fromtext))

    def handle_uploaded_file(f):
        if not os.path.exists(os.path.dirname('static/users_images/'+f.name)):
            try:
                os.makedirs(os.path.dirname('static/users_images/'+f.name))
            except OSError as exc:  # Guard against race condition
                    raise

        with open('static/users_images/'+f.name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
