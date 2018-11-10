import DynamicTopics
from memes import models
import gensim

def Start():
    list_texts = []
    list_tags = []
    memes = models.Meme.objects.all()
    for mem in memes:
        list_texts.append(mem.ru_text.split(' '))
        list_tags.append(mem.labels.split(' '))
    
    dictionary_texts = gensim.corpora.Dictionary(list_texts)
    dictionary_texts.save('dictionary_texts.dict')
    
    dictionary_tags = gensim.corpora.Dictionary(list_tags)
    dictionary_tags.save('dictionary_tags.dict')
    
    corpus_texts = [dictionary_texts.doc2bow(text) for text in list_texts]
    corpus_tags = [dictionary_tags.doc2bow(text) for text in list_tags]
    
    
    model_texts = DynamicTopics.compute_coherence_values(dictionary_texts, corpus_texts, list_texts, 1, 10)
    model_tags = DynamicTopics.compute_coherence_values(dictionary_tags, corpus_tags, list_tags, 1, 10)
    
    i = 0
    for mem in memes:
        mem.cluster_text = num_cluster(list_texts, i, model_texts, corpus_texts)
        mem.cluster_label = num_cluster(list_tags, i, model_tags, corpus_tags)
        mem.save()
        i+=1
      
    model_texts.save('model_texts.model')
    model_tags.save('model_tags.model')


def num_cluster(data, i, model, corpus):
    topic_keywords=[]
    num_t = model.get_document_topics(corpus[i])
    num_t.sort(key = lambda x: x[1], reverse = True)
    wp = model.show_topic(num_t[0][0])
    topic_keywords.append([word for word, prop in wp])
    count = 0
    for j in range(len(data[i])):
        if data[i][j] in topic_keywords[0]:
            count += 1
    if count != 0:            
        return num_t[0][0]
    else:
        return -1