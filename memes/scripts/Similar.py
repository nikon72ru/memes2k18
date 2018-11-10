import gensim

def getTopicForQuery(text, model, dictionary):

    ques_vec = dictionary.doc2bow(text)
    topic_vec = model[ques_vec]
    topic_vec = topic_vec[0]
    topic_vec.sort(key = lambda x: x[1], reverse = True)
    return topic_vec[0][0]

def Similar(text, tags):
    text = text.split(',')
    tags = tags.split(',')
    
    model_text = gensim.models.ldamodel.LdaModel.load('model_texts.model')
    model_tags = gensim.models.ldamodel.LdaModel.load('model_tags.model')
    
    
    dictionary_texts = gensim.corpora.Dictionary.load('dictionary_texts.dict')
    dictionary_tags = gensim.corpora.Dictionary.load('dictionary_tags.dict')
    
    topic_text = getTopicForQuery(text, model_text, dictionary_texts)
    
    topic_tags = getTopicForQuery(tags, model_tags, dictionary_tags)
    
    return (topic_text, topic_tags)