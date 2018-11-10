import io
import os

import pandas as pd

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

from translator import translate_raw_text
from Lemmatization import Lemmatization
from memes import models

def recognite_image(path):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.abspath("api_key.json")

    file_name = path

    # Instantiates a client
    client = vision.ImageAnnotatorClient()


    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations
    labels_to_write = []
    labels_score_to_write = []
    for label in labels:
    #labels_to_write.append((label.description, label.score))
        labels_to_write.append(label.description)
        #labels_score_to_write.append(label.score)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    texts_to_write = []
    for text in texts:
        texts_to_write.append(text.description)
    if len(texts_to_write) != 0:
        texts_to_write.pop(0)

    raw_text = translate_raw_text(str(texts_to_write))
    raw_text = Lemmatization(raw_text.split(' '))
    raw_labels = Lemmatization(labels_to_write)
#    f = open('result.csv', mode='a', encoding='utf8').write('img/' + name + '\t' + str(labels_to_write) + '\t' + str(texts_to_write)+'\n')


    models.Meme.objects.create(image_url = path, raw_text = raw_text, labels=raw_labels)

    print(path)

#recognite_image('../../memes2k18/static/img/1533111046190292958.png')

