from django.shortcuts import render

# Create your views here.

def home(request):
    context = {'generations': 'empty'}
    return render(request, 'contapp/home.html', context)