import time

import requests
import os
from memes.utils import Utils
from memes.scripts.TextSearch import textSearch

#token = 'bot690557750:AAHL9Ns7z4m7w5wegK2Ke2KXCq54tGy5Uno/'
token = 'bot727144227:AAFnLFELymt-RxcdNw2WXU8cu9Rvsh_L3SE/'

connect_url = 'https://api.telegram.org/' + token
download_url = 'https://api.telegram.org/file/' + token
file_path_url = 'https://api.telegram.org/' + token + 'getFile?file_id='
send_photo_url = "https://api.telegram.org/" + token + "sendPhoto?chat_id="

import json

json_keyboard = json.dumps({'keyboard': [["Ещё"]],
          'one_time_keyboard': True,
          'resize_keyboard': True})

def get_updates_json(request):
    response = requests.get(request+'getUpdates')
    return response.json()


def load_image(file_id):
    path = 'static/users_images/'
    result = requests.get(file_path_url + file_id).json()['result']
    r = requests.get(download_url + result['file_path'], allow_redirects=True)
    open(path + result['file_path'].split("/")[-1], 'wb').write(r.content)
    return result['file_path'].split("/")[-1]


def last_update(data, last_message_id, pathes):
    results = data['result']
    #print(results)
    total_updates = len(results) - 1
    if results[total_updates]['message']['message_id'] == last_message_id:
        print("Old Message")
        print(last_message_id)
        return results[total_updates], 'NoWay', last_message_id
    path = 'file_0.jpg'
    if 'photo' in results[total_updates]['message']:
        print('In photos')
        n = len(results[total_updates]['message']['photo'])
        path = load_image(results[total_updates]['message']['photo'][n-1]['file_id'])
    if 'text' in results[total_updates]['message'] and results[total_updates]['message']['text'] == 'Ещё':
        print('In More')
        chat_id = get_chat_id(results[total_updates])
        # mess_data = recognite_image_no_save(path)
        if len(pathes) == 0:
            print('Empty pathes')
            return results[total_updates], 'NoWay', results[total_updates]['message']['message_id']
        send_image(chat_id, pathes[0])
        pathes[:] = pathes[1:]
        send_mess(chat_id, "")
        return results[total_updates], 'NoWay', results[total_updates]['message']['message_id']
    if 'text' in results[total_updates]['message']:
        print('In Text')
        id = textSearch(results[total_updates]['message']['text'])
        pathes[:] = get_image_similars_text(id)
        chat_id = get_chat_id(results[total_updates])
        send_image(chat_id, pathes[0])
        pathes[:] = pathes[1:]
        send_mess(chat_id, "")
        return results[total_updates], 'NoWay', results[total_updates]['message']['message_id']


    return results[total_updates], path, results[total_updates]['message']['message_id']

def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id

def send_mess(chat, text):
    params = {'chat_id': chat, 'text': "Ещё?", 'reply_markup':json_keyboard}
    response = requests.post(connect_url + 'sendMessage', data=params)
    return response

def send_image(chat, file_name):
    path = file_name.replace('/', '', 1)
    files = {'photo': open(path, 'rb')}
    status = requests.post(send_photo_url + str(chat), files=files)

def get_image_similars(path):
    res = Utils.getForFindAll(path)
    pathes = [i.image_url for i in res]
    return pathes

def get_image_similars_text(id):
    res = Utils.getFromClusterText(id, 0, 9999)
    pathes = [i.image_url for i in res]
    return pathes

# proxy = 'http://<user>:<pass>@<proxy>:<port>'
#proxy = 'http://193.160.226.89:53186'
proxy = 'http://158.181.19.142:57461'


def runBot():
    os.environ['http_proxy'] = proxy
    os.environ['HTTP_PROXY'] = proxy
    os.environ['https_proxy'] = proxy
    os.environ['HTTPS_PROXY'] = proxy

    last_message_id = 0
    pathes_to_push = []

    while True:
        print('Work')
        update, path, last_message_id = last_update(get_updates_json(connect_url), last_message_id, pathes_to_push)
        if path != 'NoWay':
            print("No Pathes")
            chat_id = get_chat_id(update)
            pathes_to_push = get_image_similars(path)
            #mess_data = recognite_image_no_save(path)
            send_image(chat_id, pathes_to_push[0])
            pathes_to_push = pathes_to_push[1:]
            send_mess(chat_id, "")

        time.sleep(5)

