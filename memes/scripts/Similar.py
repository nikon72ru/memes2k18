import gensim
from memes import models


def getTopicForQuery(text, model, dictionary):
    topic_i = []
    key_words_weight = 0
    for num in range(model.num_topics):
        for j in range(len(text)):
            for word, prop in model.show_topic(num):
                if text[j] == word:
                    key_words_weight += prop
        topic_i.append(key_words_weight)
        key_words_weight = 0
    
    if max(topic_i) != 0:
        return topic_i.index(max(topic_i))
    else:
        return -1
    
#    topic_keywords = []
#    ques_vec = dictionary.doc2bow(text)
#    topic_vec = model[ques_vec]
#    topic_vec = topic_vec[0]
#    topic_vec.sort(key = lambda x: x[1], reverse = True)
#    wp = model.show_topic(topic_vec[0][0])
#    topic_keywords.append([word for word, prop in wp])
#    count = 0
#    for j in range(len(text)):
#        if text[j] in topic_keywords[0]:
#            count += 1
#    if count != 0:        
#        return topic_vec[0][0]
#    else:
#        return -1

def Similar(text, tags):
    text = text.split(',')
    tags = tags.split(',')
    
    model_text = gensim.models.ldamodel.LdaModel.load('model_texts.model')
    model_tags = gensim.models.ldamodel.LdaModel.load('model_tags.model')
    
    
    dictionary_texts = gensim.corpora.Dictionary.load('dictionary_texts.dict')
    dictionary_tags = gensim.corpora.Dictionary.load('dictionary_tags.dict')
    
    topic_text = getTopicForQuery(text, model_text, dictionary_texts)
    
    topic_tags = getTopicForQuery(tags, model_tags, dictionary_tags)
    
    requests_cluster = models.Cluster.objects.get(name=topic_text, type = 'text')
    requests_cluster.requests += 1
    requests_cluster.save()
    
    requests_cluster = models.Cluster.objects.get(name=topic_tags, type = 'tag')
    requests_cluster.requests += 1
    requests_cluster.save()
    
    return (topic_text, topic_tags)