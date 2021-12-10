from django_unicorn.components import UnicornView
import requests
from bs4 import BeautifulSoup

class ContcompView(UnicornView):
    url = "https://example.com"
    headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
    cuenta = dict()
    palabras = []

    def count(self,*args,**kwargs):
        self.page = requests.get(self.url)
        self.data = self.page.text
        self.soup = BeautifulSoup(self.data,features="html.parser")
        self.text = self.soup.get_text()
        self.palabras = self.text.split()
        self.auxpalabras = []
        for palabra in self.palabras:
            if palabra in self.cuenta:
                self.cuenta[palabra] += 1
            else:
                self.cuenta[palabra] = 1
                self.auxpalabras.append(palabra)
        self.palabras = self.auxpalabras

#TODO: Ordenar por palabras mas repeditas