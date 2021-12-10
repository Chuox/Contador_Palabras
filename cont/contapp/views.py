from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from .models import Palabras
import requests
from bs4 import BeautifulSoup

# Create your views here.

class ContCreateView(CreateView):
    model = Palabras
    fields = ['url']
    template_name = 'contapp/cont_form.html'

    def form_valid(self, form):
        if form.instance.url.startswith('http://') or form.instance.url.startswith('https://'):
            url = form.instance.url
        else:
            url = "http://" +form.instance.url
        page = requests.get(url)
        data = page.text
        soup = BeautifulSoup(data,features="html.parser")
        self.text = soup.get_text()
        form.instance.texto = self.text
        return super().form_valid(form)

class ContDetailView(DetailView):
    model = Palabras

    def get_context_data(self, **kwargs):
        context = super(ContDetailView, self).get_context_data(**kwargs)
        cuenta = dict()
        palabras = Palabras.objects.get(id=self.object.id).texto.split()
        for palabra in palabras:
            if palabra in cuenta:
                cuenta[palabra] += 1
            else:
                cuenta[palabra] = 1

        context['palabras'] = dict(sorted(cuenta.items(), key=lambda item: item[1], reverse=True)) #cuenta #Palabras.objects.get(id=self.object.id).texto
        return context
