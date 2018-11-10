import io
import os


# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

from memes.scripts.translator import translate_raw_text
from memes.scripts.Lemmatization import Lemmatization
from memes.scripts.Similar import Similar
from memes.scripts.Preprocessings import Preprocessings_phrase
from memes import models

def recognite_image(path):
    print(path)
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


    models.Meme.objects.create(image_url = path, raw_text = str(raw_text).replace('[','').replace(']','').replace("'",'').replace(',', ' '), labels=str(raw_labels).replace('[','').replace(']','').replace("'",'').replace(',', ' '))

    print(path)

#recognite_image('../../memes2k18/static/img/1533111046190292958.png')

def recognite_image_no_save(path):
    print(path)
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
    print(path)
    return raw_text

def recognite_image_cluster(file_name):
    path = 'static/users_images/' + file_name
    print(path)
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

    raw_text = Preprocessings_phrase(str(raw_text).replace('[','').replace(']','').replace("'",'').replace(',', ' '))
    result = Similar(str(raw_text).replace('[','').replace(']','').replace("'",''), str(raw_labels).replace('[','').replace(']','').replace("'",''))
    
    return result

#recognite_image_cluster('15350881881447498.jpg')

