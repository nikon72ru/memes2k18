import os
from random import randint

from memes import models
from itertools import chain
from memes.scripts.recognition import recognite_image_cluster

class Utils:
    def getHottest(offset):
        count=10
        firstCount = int(count*0.2)
        secondCount = int(count*0.3)
        counts = [count-firstCount-secondCount, secondCount, firstCount]
        pictures = []
        clusters = models.Cluster.objects.filter(type='tag').order_by('-requests').all()[:3]
        print(clusters)
        i=0
        for cluster in clusters:
            print(cluster.id)
            pctrs = models.Meme.objects.filter(cluster_label_id=cluster.id)[int(offset):int(offset)+counts[i]]
            print(pctrs)
            i += 1
            pictures = list(chain(pictures, pctrs))
            print(pictures)
        #     for pic in pctrs:
        #         pictures.append(pic.image_url)
        #
        return pictures

    def getFresh(offset):
        return models.Meme.objects.order_by('-created_at')[int(offset):int(offset)+10]

    def getFromClusterText(id, offset, count):
        cl = models.Cluster.objects.filter(name=id, type='text').last()
        print(cl.id)
        return models.Meme.objects.order_by('-created_at').filter(cluster_text=cl)[int(offset):int(offset)+count]

    def getFromClusterLabel(id, offset, count):
        cl = models.Cluster.objects.filter(name=id, type='tag').last()
        return models.Meme.objects.order_by('-created_at').filter(cluster_label=cl)[int(offset):int(offset)+count]

    def getForFind(filter, offset):
        if (filter==""):
            return  models.Meme.objects.order_by('?')[:10]
        clusters = filter.split(',')
        if (len(clusters) == 1):
            return Utils.getFromClusterText(clusters[0], offset, 10)
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
