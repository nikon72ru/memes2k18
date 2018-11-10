import memes.scripts.Preprocessings as Preprocessings
import gensim
from memes import models

def getTopicForQuery(text, model, dictionary):
    topic_keywords = []
    ques_vec = dictionary.doc2bow(text)
    topic_vec = model[ques_vec]
    topic_vec = topic_vec[0]
    topic_vec.sort(key = lambda x: x[1], reverse = True)
    wp = model.show_topic(topic_vec[0][0])
    topic_keywords.append([word for word, prop in wp])
    count = 0
    for j in range(len(text)):
        if text[j] in topic_keywords[0]:
            count += 1
    if count != 0:        
        return topic_vec[0][0]
    else:
        return -1

def textSearch(text):
    text = Preprocessings.Preprocessings_phrase(text)
    
    model_text = gensim.models.ldamodel.LdaModel.load('model_texts.model')    
    
    dictionary_texts = gensim.corpora.Dictionary.load('dictionary_texts.dict')
    
    topic_cluster = getTopicForQuery(text, model_text, dictionary_texts)    
    requests_cluster = models.Cluster.objects.get(name=topic_cluster, type = 'text')
    requests_cluster.requests += 1
    requests_cluster.save()
    
    return topic_cluster

    
    
    