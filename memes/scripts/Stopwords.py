def Remove_Stopwords(phrase: list, stopwords_path):
    # text_file = open(stopwords_path, "r")
    # stop_words = text_file.read().lower().split('\n')
    # text_file.close()
    stop_words = [
        'а', 'б'
    ]
    filtered_word_list = phrase[:]
    for word in phrase:
        if word in stop_words: 
            filtered_word_list.remove(word)
    return filtered_word_list