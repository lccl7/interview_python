#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

url = 'https://www.douban.com/doulist/176513/'
url_data = requests.get(url)
soup = BeautifulSoup(url_data.text, 'lxml')
titles = soup.select('div.title > a')
imgs =  soup.select('img[width="100"]')
rates = soup.select('div.rating > span.rating_nums')
authors = soup.select('div.abstract')
comments = soup.select('div.comment-item.content > blockquote')
#for title in titles:
    #print title.get_text().strip() + ' rate:' + rate.get_text().strip()
L = []
for title, rate, author in zip(titles, rates, authors):
    data = {
        'title': title.get_text().strip(),
        'rate': rate.get_text().strip(),
        'author':author.get_text().strip().replace(' ', '*'),
    #    'comment':comment.get_text().strip()
    }
    print data

'''
for title, img, rate, author, comment in zip(titles, imgs, rates, authors, comments):
    data = {
        title: title.get_text(),
        img: img.get('src'),
        rate: rate.get_text(),
        author:author.get_text(),
        comment: comment.get_text()
    }
'''
#print(titles,imgs,rates)
#*[@id="item1167928"]/div/div[2]/div[6]/text()[1]
#item1167946 > div > div.bd.doulist-subject > div.abstract
#item1167946 > div > div.ft > div.comment-item.content > blockquote
#item1167946 > div > div.bd.doulist-subject > div.rating > span.rating_nums
#item1167946 > div > div.bd.doulist-subject > div.title > a
