import memes.scripts.Preprocessings as Preprocessings
from memes import models


def Preprocessings_data():
    memes = models.Meme.objects.all()
    for mem in memes:
        mem.lem_text = ' '.join(Preprocessings.Preprocessings_phrase(mem.raw_text))
        mem.save()
