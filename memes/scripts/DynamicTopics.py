import gensim
def compute_coherence_values(dictionary, corpus, texts, start, step):
    coherence_values = []
    num_topics = start;
    flag = True
    
    model = New_model(corpus, num_topics, dictionary, 150, 200, 50, 0.15, 0.75, True)    
    coherence_values.append(New_coherencemodel(model = model, texts = texts, dictionary = dictionary, coherence = 'u_mass'))
    
    num_topics += step;
    model = New_model(corpus, num_topics, dictionary, 150, 200, 50, 0.15, 0.75, True)
    coherence_values.append(New_coherencemodel(model = model, texts = texts, dictionary = dictionary, coherence = 'u_mass'))
    if(coherence_values[-1] - coherence_values[-2] <= 0.01):
        flag = False
        return model
    num_topics += step;
    while(flag):         
        model = New_model(corpus, num_topics, dictionary, 150, 200, 50, 0.15, 0.75, True)
        coh = New_coherencemodel(model = model, texts = texts, dictionary = dictionary, coherence = 'u_mass')
        if(coherence_values[-1] - coh <= 0.01):
            return model
        coherence_values.append(coh)
        num_topics += step;
        
def New_model(corpus, num_topics, dictionary, random_state, chunksize, passes, alpha, eta, per_word_topics):
    return gensim.models.ldamodel.LdaModel(corpus = corpus, 
                                            num_topics = num_topics, 
                                            id2word = dictionary,
                                            random_state = random_state,
                                            chunksize = chunksize,
                                            passes = passes, 
                                            alpha = alpha,
                                            eta = eta,
                                            per_word_topics = per_word_topics)
    
def New_coherencemodel(model, texts, dictionary, coherence):
    coherencemodel = gensim.models.coherencemodel.CoherenceModel(model = model,
                                                       texts = texts,
                                                       dictionary = dictionary,
                                                       coherence = coherence)
    return coherencemodel.get_coherence()