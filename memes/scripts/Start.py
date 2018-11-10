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
        
    bigram = gensim.models.Phrases(list_texts, min_count=5, threshold=20)
    bigram_mod = gensim.models.phrases.Phraser(bigram)
    def make_bigrams(texts):
        return [bigram_mod[doc] for doc in texts]

    bigrams_texts = make_bigrams(list_texts)
    dictionary_texts = gensim.corpora.Dictionary(bigrams_texts)
    dictionary_texts.save('dictionary_texts.dict')
    
    dictionary_tags = gensim.corpora.Dictionary(list_tags)
    dictionary_tags.save('dictionary_tags.dict')
    
    corpus_texts = [dictionary_texts.doc2bow(text) for text in bigrams_texts]
    corpus_tags = [dictionary_tags.doc2bow(text) for text in list_tags]
    
    
    model_texts = DynamicTopics.compute_coherence_values(dictionary_texts, corpus_texts, bigrams_texts, 1, 10)
    model_tags = DynamicTopics.compute_coherence_values(dictionary_tags, corpus_tags, list_tags, 1, 10)

    vis1 = pyLDAvis.gensim.prepare(model_texts, corpus_texts, dictionary_texts, sort_topics = False)
    pyLDAvis.save_html(vis1, 'text_model.html')
    
    vis2 = pyLDAvis.gensim.prepare(model_tags, corpus_tags, dictionary_tags, sort_topics = False)
    pyLDAvis.save_html(vis2, 'tag_model.html')
    
#    for num in range(model_texts.num_topics):
#        models.Cluster.objects.create(name = num, requests = 0, type = "text")
#    for num in range(model_tags.num_topics):
#        models.Cluster.objects.create(name = num, requests = 0, type = "tag")
#    models.Cluster.objects.create(name = '-1', requests = 0, type = "text")   
#    models.Cluster.objects.create(name = '-1', requests = 0, type = "tag")
    i = 0
    count_one = 0
    count_two = 0
    for mem in memes:
        if(list_texts[i] != []):
            res = num_cluster(list_texts, i, model_texts, corpus_texts)
            
            mem.cluster_text = models.Cluster.objects.get(name=res, type = 'text')
            if (res == -1): count_one += 1
        if(list_tags[i] != []):
            res = num_cluster(list_tags, i, model_tags, corpus_tags)
            mem.cluster_label = models.Cluster.objects.get(name=res, type = 'tag')
            if (res == -1): count_two += 1
        mem.save()
        i+=1
        
    print(count_one, count_two)
      
#    model_texts.save('model_texts.model')
#    model_tags.save('model_tags.model')

    
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