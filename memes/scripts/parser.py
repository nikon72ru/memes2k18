import time
import requests

import selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def load_images():
    path = '../../memes2k18/static/img/'
    browser = webdriver.Chrome()

    browser.get("https://pikabu.ru/tag/мемы")
    time.sleep(1)

    elem = browser.find_element_by_tag_name("body")

    no_of_pagedowns = 30000
    all_memes = dict()
    while no_of_pagedowns:
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)
        buffer_elements = browser.find_elements_by_class_name("story")
        for post in buffer_elements:
            if post in all_memes:
                continue
            else:
                try:
                    a = dict()
                    tags = post.find_elements_by_class_name('tags__tag')
                    a['tags'] = [i.text for i in tags]
                    url_of_img = post.find_element_by_class_name('story-image__content').find_element_by_tag_name('img').get_attribute('src')
                    a['url'] = url_of_img
                    r = requests.get(url_of_img, allow_redirects=True)
                    open(path + url_of_img.split("/")[-1], 'wb').write(r.content)
                    all_memes[post] = a
                    #f = open('result.csv', 'a').write('img/' + url_of_img.split("/")[-1] + '\t' + str(a['tags']) + '\n')
                except: print('mistake')
        no_of_pagedowns -= 1

    post_elems = browser.find_elements_by_class_name("story")
