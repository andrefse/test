# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 11:04:48 2020

@author: Andre
"""

from urllib.request import urlopen

def getSource(url):
    response = urlopen(url)
    html = response.read()
    return html.decode()

html = getSource('http://www.uol.com.br')
#print(html)

# parser inicialmente não faz nada
from html.parser import HTMLParser

#necessário estender a classeHTMLParse para trazer funcionalidade a um handler
class MyParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag =='a':
            for attr in attrs:
                if attr[0] == 'href':
                    print(attr[1])

parser = MyParser()
parser.feed(html)
#vai imprimir todos os links d tad a que tenha href

