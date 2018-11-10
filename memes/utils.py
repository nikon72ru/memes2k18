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

