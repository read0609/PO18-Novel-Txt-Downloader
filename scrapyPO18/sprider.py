# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

def parser_html(html):
    chapter = html.replace("&nbsp;&nbsp;", '')
    soup = BeautifulSoup(chapter, 'lxml')
    chapter_title = soup.find('h1').get_text()
    txt.write(chapter_title + '\n')
    text = soup.find_all(name='p')
    for row in text:
        txt.write(row.get_text())
    print('%s done.' % chapter_title)

def read_html_txt(original_html_txt):
    with open(original_html_txt, 'r', encoding='utf-8') as f:
        html = f.read()
        return html

book_name = '初戀'
# content_url = 'https://www.po18.tw/books/' + book_number + '/articles'
# chapter_sum = 161
# start = 3
original_max = 6
txt = open(book_name + '.txt', 'a')
for i in range(1, original_max + 1):
    html = read_html_txt('./original_html_txt/' + str(i) + '.txt')
    parser_html(html)
txt.close()
