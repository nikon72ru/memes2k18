import memes.scripts.DynamicTopics as DynamicTopics
import memes.scripts.Preprocessings as Preprocessings
from memes import models
import gensim
import pyLDAvis.gensim
pyLDAvis.enable_notebook()

def Start():
    list_texts = []
    list_tags = []
    memes = models.Meme.objects.all()
    for mem in memes:
        list_texts.append(' '.join(mem.lem_text.split(' ')).split())   
        list_tags.append(' '.join(mem.labels.split(' ')).split())    
    
    dictionary_texts = gensim.corpora.Dictionary(list_texts)
    dictionary_texts.save('dictionary_texts.dict')
    
    dictionary_tags = gensim.corpora.Dictionary(list_tags)
    dictionary_tags.save('dictionary_tags.dict')
    
    corpus_texts = [dictionary_texts.doc2bow(text) for text in list_texts]
    corpus_tags = [dictionary_tags.doc2bow(text) for text in list_tags]
    
    model_texts = DynamicTopics.compute_coherence_values(dictionary_texts, corpus_texts, list_texts, 1, 10)
    model_tags = DynamicTopics.compute_coherence_values(dictionary_tags, corpus_tags, list_tags, 1, 10)
    
    for num in range(model_texts.num_topics):
        models.Cluster.objects.create(name = num, requests = 0, type = "text")
    for num in range(model_tags.num_topics):
        models.Cluster.objects.create(name = num, requests = 0, type = "tag")
    models.Cluster.objects.create(name = '-1', requests = 0, type = "text")   
    models.Cluster.objects.create(name = '-1', requests = 0, type = "tag")
    
    i = 0
    for mem in memes:
        if(list_texts[i] != []):
            res = num_cluster(list_texts[i], i, model_texts, list_texts) 
            mem.cluster_text = models.Cluster.objects.filter(name=res, type = 'text').last()
        else:
            mem.cluster_text = None
        if(list_tags[i] != []):
            res = num_cluster(list_tags[i], i, model_tags, list_tags)
            mem.cluster_label = models.Cluster.objects.filter(name=res, type = 'tag').last()
        else:
            mem.cluster_text = None        
        
        mem.save()
        i+=1
      
    model_texts.save('model_texts.model')
    model_tags.save('model_tags.model')

    
def num_cluster(data, i, model, list_data):
    topic_i = []
    key_words_weight = 0
    for num in range(model.num_topics):
        for j in range(len(data)):
            for word, prop in model.show_topic(num):
                if data[j] == word:
                    key_words_weight += prop
        topic_i.append(key_words_weight)
        key_words_weight = 0
    
    if max(topic_i) != 0:
        return topic_i.index(max(topic_i))
    else:
        return -1