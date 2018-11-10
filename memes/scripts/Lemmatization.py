def Lemmatization(phrase: list):
    import pymorphy2
    morph = pymorphy2.MorphAnalyzer()
    data = []
    for word in phrase:
        data.append(morph.parse(word)[0].normal_form)
    return data