def Remove_Stopwords(phrase: list, stopwords_path):
    # text_file = open(stopwords_path, "r")
    # stop_words = text_file.read().lower().split('\n')
    # text_file.close()
    stop_words = [
        'й','ц','у','к','е','н','г','ш','щ','з','х','ъ','ф','ы','в','а','п','р','о','л','д','ж','э','я','ч','с','м','и','т','ь','б','ю','то','на','не','ни','об','но','он','свой','мне','мои','мож','она','они','оно','мной','много','многочисленное','многочисленная','многочисленные','многочисленный','мною','мой','мог','могут','можно','может','можхо','мор','моя','моё','мочь','над','нее','оба','нам','нем','нами','ними','мимо','немного','одной','одного','менее','однажды','однако','меня','нему','меньше','ней','наверху','него','ниже','мало','надо','один','одиннадцать','одиннадцатый','назад','наиболее','недавно','миллионов','недалеко','между','низко','меля','нибудь','непрерывно','наконец','никогда','никуда','нас','наш','нет','нею','неё','них','мира','наша','наше','наши','ничего','начала','нередко','несколько','обычно','опять','около','мы','ну','нх','от','отовсюду','особенно','нужно','очень','отсюда','во','вон','вниз','внизу','вокруг','вот','восемнадцать','восемнадцатый','восемь','восьмой','вверх','вам','вами','важное','важная','важные','важный','вдали','везде','ведь','вас','ваш','ваша','ваше','ваши','впрочем','весь','вдруг','вы','все','второй','всем','всеми','времени','время','всему','всего','всегда','всех','всею','всю','вся','всё','всюду','год','говорил','говорит','года','году','где','да','ее','за','из','ли','же','им','до','по','ими','под','иногда','довольно','именно','долго','позже','более','должно','пожалуйста','значит','иметь','больше','пока','ему','имя','пор','пора','потом','потому','после','почему','почти','посреди','ей','два','две','двенадцать','двенадцатый','двадцать','двадцатый','двух','его','дел','или','без','день','занят','занята','занято','заняты','действительно','давно','девятнадцать','девятнадцатый','девять','девятый','даже','алло','жизнь','далеко','близко','здесь','дальше','для','лет','зато','даром','первый','перед','затем','зачем','лишь','десять','десятый','ею','её','их','бы','еще','при','был','про','процентов','против','бывает','бывь','если','люди','была','были','было','будем','будет','будете','будешь','прекрасно','буду','будь','будто','будут','ещё','пятнадцать','пятнадцатый','друго','другое','другой','другие','другая','других','есть','пять','быть','лучше','пятый','ком','конечно','кому','кого','когда','которой','которого','которая','которые','который','которых','кем','каждое','каждая','каждые','каждый','кажется','как','какой','какая','кто','кроме','куда','кругом','та','те','уж','со','том','снова','тому','совсем','того','тогда','тоже','собой','тобой','собою','тобою','сначала','только','уметь','тот','тою','хорошо','хотеть','хочешь','хоть','хотя','свое','свои','твой','своей','своего','своих','свою','твоя','твоё','раз','уже','сам','там','тем','чем','сама','сами','теми','само','рано','самом','самому','самой','самого','семнадцать','семнадцатый','самим','самими','самих','саму','семь','чему','раньше','сейчас','чего','сегодня','себе','тебе','сеаой','человек','разве','теперь','себя','тебя','седьмой','спасибо','слишком','так','такое','такой','такие','также','такая','сих','тех','чаще','четвертый','через','часто','шестой','шестнадцать','шестнадцатый','шесть','четыре','четырнадцать','четырнадцатый','сколько','сказал','сказала','сказать','ту','ты','три','эта','эти','что','это','чтоб','этом','этому','этой','этого','чтобы','этот','стал','туда','этим','этими','рядом','тринадцать','тринадцатый','этих','третий','тут','эту','суть','чуть','тысяч','мм','мин'
    ]
    filtered_word_list = phrase[:]
    for word in phrase:
        if word in stop_words: 
            filtered_word_list.remove(word)
    return filtered_word_list