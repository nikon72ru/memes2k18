def Tokenization(phrase: str):
    import nltk
    import string
    tokens = nltk.wordpunct_tokenize(phrase)
    data = []
    bit_tok = "" 
    
    for bit in tokens:
        for i in bit:
            if (i not in string.digits):
                if (i not in string.punctuation):
                    if i == 'ё':
                        bit_tok += 'е'
                    else:
                        bit_tok += i
                else:
                    bit_tok += " "
                    break
            else:
                    bit_tok += " "
                    break
        if bit_tok != "" or bit_tok != " ":
            data.append(bit_tok.lower().strip())
            bit_tok = ""
    
    tokens = [i.replace("«", "").replace("»", "") for i in tokens]
    return data