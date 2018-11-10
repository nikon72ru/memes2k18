import Lemmatization
import Tokenization
import Stopwords
def Preprocessings_phrase(phrase: str):
    new_phrase = Tokenization.Tokenization(phrase)
    new_phrase = Lemmatization.Lemmatization(new_phrase)
    new_phrase = Stopwords.Remove_Stopwords(new_phrase, 'Stop.txt')
    return new_phrase

def Preprocessings_list_phrase(dataFrame):
    df = []
    for i in range(len(dataFrame)):
        df.append(Preprocessings_phrase(dataFrame['Texts'][i]))
    dataFrame['Lemmatized'] = df
    return dataFrame