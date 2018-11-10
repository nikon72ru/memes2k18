import io
import os

import pandas as pd

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types


def recognite_images(df, path):
    #files = os.listdir(path)
    col_names = ['names', 'labels', 'texts']
    #df = pd.DataFrame(columns=col_names)
    for i, row in df.iterrows():

        # The name of the image file to annotate
        file_name = path + df

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
        f = open('result.csv', mode='a', encoding='utf8').write('img/' + name + '\t' + str(labels_to_write) + '\t' + str(texts_to_write)+'\n')
        df.loc[len(df)] = [name, str(labels_to_write), str(texts_to_write)]
        print(name)


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
#    f = open('result.csv', mode='a', encoding='utf8').write('img/' + name + '\t' + str(labels_to_write) + '\t' + str(texts_to_write)+'\n')
    print(path)

recognite_image('C:/Users/tanok/Desktop/memes2k18/memes2k18/static/img/153313659812790.jpg')

