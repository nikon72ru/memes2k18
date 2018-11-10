import re

import requests
import json
import pandas as pd


check_lang_url = 'https://translate.yandex.net/api/v1.5/tr.json/detect?key=trnsl.1.1.20181109T142619Z.ab3db7ff0f9b9c6a.e38405c416e11e05beac9c020deaf8da7cb9c46a'
translate_url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20181109T142619Z.ab3db7ff0f9b9c6a.e38405c416e11e05beac9c020deaf8da7cb9c46a&lang=en-ru'


def check_lang(word):
    r = requests.get(check_lang_url + '&' + 'text=' + str(word) + '&' + 'hint=en')
    lang = json.loads(r.text)
    return lang['lang']


def translate_word(word):
    r = requests.get(translate_url + '&' + 'text=' + str(word))
    trans = json.loads(r.text)
    return trans['text']


def translate_dataframe(df):
    df = df.dropna()
    for j, row in df.iterrows():
        i = row['texts']
        i = i.replace("'", '')
        i = i.replace('.', '')
        i = i.replace('#', '')
        i = i.replace('"', '')
        i = i.replace('?', '')
        i = i.replace('!', '')
        i = i.replace('@', '')
        i = i.replace('(', '')
        i = i.replace(')', '')
        i = i.replace('-', '')
        i = i.replace('_', '')
        i = i.replace(':', '')
        i = i.replace('+', '')
        i = i.replace('-', '')
        i = i.replace('--', '')
        i = i.replace('=', '')
        i = i.replace('*', '')
        i = i.replace('&', '')
        i = i.replace('|', '')
        i = i.replace('%', '')
        i = i.replace('/', '')
        i = i.replace('\\', '')


        print(i)
        str_to_translate = i.split(',')
        str_to_translate = [value for value in str_to_translate if value != '']
        # str_to_translate.remove('')
        for word in str_to_translate:
            lang = check_lang(str(word))
            if lang == 'ru':
                continue
            elif lang == 'en':
                translate = translate_word(str(word))
                if check_lang(translate) == 'en':
                    # i = i.replace(str(word), '')
                    i = re.sub(r"\b%s\b" % str(word),'',i)
                else:
                    prog = re.compile('[A_Za-z]')
                    if bool(prog.match(str(translate))):
                        # i = i.replace(str(word), '')
                        i = re.sub(r"\b%s\b" % str(word), '', i)
                    else:
                        # i = i.replace(str(word), str(translate))
                        i = re.sub(r"\b%s\b" % str(word), str(translate), i)
            else:
                # i = i.replace(str(word), '')
                i = re.sub(r"\b%s\b" % str(word), '', i)
            i = i.replace('[', '').replace(']', '')
        i = i.replace("'", '')
        i = i.replace('"', '')
        df.at[j,'texts'] = i
        print(i)

#    print(df.to_csv('resultNew.csv'))
    return df


def translate_raw_text(raw_text):
    i = raw_text
    i = i.replace('[', '')
    i = i.replace(']', '')
    i = i.replace("'", '')
    i = i.replace('.', '')
    i = i.replace('#', '')
    i = i.replace('"', '')
    i = i.replace('?', '')
    i = i.replace('!', '')
    i = i.replace('@', '')
    i = i.replace('(', '')
    i = i.replace(')', '')
    i = i.replace('-', '')
    i = i.replace('_', '')
    i = i.replace(':', '')
    i = i.replace('+', '')
    i = i.replace('-', '')
    i = i.replace('--', '')
    i = i.replace('=', '')
    i = i.replace('*', '')
    i = i.replace('&', '')
    i = i.replace('|', '')
    i = i.replace('%', '')
    i = i.replace('/', '')
    i = i.replace('\\', '')
    i = i.replace(',', ' ')

    print(i)
    str_to_translate = i.split(' ')
    str_to_translate = [value for value in str_to_translate if value != '']
    # str_to_translate.remove('')
    for word in str_to_translate:
        lang = check_lang(str(word))
        if lang == 'ru':
            continue
        elif lang == 'en':
            translate = translate_word(str(word))
            if check_lang(translate) == 'en':
                # i = i.replace(str(word), '')
                i = re.sub(r"\b%s\b" % str(word),'',i)
            else:
                prog = re.compile('[A_Za-z]')
                if bool(prog.match(str(translate))):
                # i = i.replace(str(word), '')
                    i = re.sub(r"\b%s\b" % str(word), '', i)
                else:
                # i = i.replace(str(word), str(translate))
                    i = re.sub(r"\b%s\b" % str(word), str(translate), i)
        else:
        # i = i.replace(str(word), '')
            i = re.sub(r"\b%s\b" % str(word), '', i)
        i = i.replace('[', '').replace(']', '')
        i = i.replace("'", '')
        i = i.replace('"', '')

    return i.replace(',', ' ')